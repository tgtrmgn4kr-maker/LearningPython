import argparse

parser = argparse.ArgumentParser()

parser.add_argument('url', help='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

args = parser.parse_args()

print(f'URL: {args.url}')

