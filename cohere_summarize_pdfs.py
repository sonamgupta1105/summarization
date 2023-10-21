#### Idea is to use Cohere's co:summarize endpoint to summarize ACL short papers

# Command to run the script: python cohere_summarize_pdfs.py -m summarize-medium -l medium -e high -t 0.8 -f paragraph

# Import libraries
import cohere
import argparse

# Set up Cohere client using API key

co = cohere.Client('your-api-key')

# Read the text file
with open('output.txt', 'r', encoding="mbcs") as f:
    generate_datasets = f.read().replace('\n', '')

# Arguments to parse through command line to run different values for each parameter in the summarize()

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--model", type=str, help = "Choose between summarize-medium or summarize-xlarge")
argParser.add_argument("-l", "--length", type=str, help = "Choose between short, medium, long")
argParser.add_argument("-e", "--extractiveness", type = str, help = "Choose between low, medium, high")
argParser.add_argument("-t", "--temperature", type = float, help = "Choose between 0.5, 0.8, 1, 1.5, 2")
argParser.add_argument("-f", "--format", type = str, help = "Choose between paragraph and bullets")

# Parse the arguments
args = argParser.parse_args()
print("args=%s" % args)

# Call the summarize endpoint from Cohere and provide parameters
response = co.summarize(
    text = generate_datasets, 
    model = args.model, 
    length = args.length,
    extractiveness = args.extractiveness,
    temperature = args.temperature,
    format = args.format
)
print(response)
