import os
import sys
import argparse
import shutil
import pandas as pd
import numpy as np

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--infile', type=str, required=True, help="Argument passed by Edge Impulse transformation block when the --infile option is selected")
parser.add_argument('--outdirectory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --outdirectory option is selected")
parser.add_argument('--splitinterval', type=int, required=True, help="Time interval in seconds for splitting the CSV")
parser.add_argument('--timecolumn', type=str, required=True, help="Name of the time column in the CSV")

args, unknown = parser.parse_known_args()
print('--infile: ', args.in_file, flush=True)
print('--outdirectory: ', args.out_directory, flush=True)
print('--splitinterval: ', args.split_interval, flush=True)
print('--timecolumn: ', args.time_column, flush=True)

# 
if args.in_file:
    if not os.path.exists(args.in_file):
        print('--infile argument', args.in_file, 'does not exist', flush=True)
    else:
        print('--infile path', args.in_file, 'exists', flush=True)
        print("filename: ", os.path.basename(args.in_file))

        # 
        df = pd.read_csv(args.in_file)
        # 
        df[args.time_column] = pd.to_datetime(df[args.time_column], unit='ns')
        # 
        df.set_index('time', inplace=True)

        # 
        def split_dataframe(df, split_interval_seconds):
            split_dataframes = []
            start_time = df.index[0]
            # 
            while start_time < df.index[-1]:
                #
                end_time = start_time + pd.Timedelta(seconds=split_interval_seconds)
                split_df = df[(df.index >= start_time) & (df.index < end_time)]
                split_dataframes.append(split_df)
                # 
                start_unix_timestamp = int(start_time.timestamp())
                end_unix_timestamp = int(end_time.timestamp())
                # 
                output_filename = os.path.join(args.out_directory, f"{os.path.splitext(os.path.basename(args.in_file))[0]}.split_{start_unix_timestamp}_{end_unix_timestamp}.csv")
                split_df.to_csv(output_filename)
                print(f"Saved {output_filename}", flush=True)
                start_time = end_time
            return split_dataframes

        # 
        split_dataframes = split_dataframe(df, args.split_interval)

        print("Finished", flush=True)
        exit(0)
else:
    print('Missing argument --infile not exist')
    sys.exit(1)
