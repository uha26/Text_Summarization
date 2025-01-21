from transformers import pipeline

# Load pre-trained summarization model
summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text, chunk_size=800):
    """
    Summarizes the input text using the pre-trained summarization model.
    The input text is split into chunks if it exceeds the max sequence length.

    Args:
        text (str): The text to be summarized.
        chunk_size (int): Maximum chunk size for each part of text.

    Returns:
        str: The summarized text.
    """
    # Split text into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []

    for chunk in chunks:
        try:
            summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            summaries.append(f"Error summarizing chunk: {str(e)}")
    
    # Join summarized chunks into one summary
    summary_text = " ".join(summaries)
    
    # Capitalize after each full stop
    summary_text = '. '.join([sentence.strip().capitalize() for sentence in summary_text.split('. ')])
    
    return summary_text

if __name__ == "__main__":
    print("Welcome to the Text Summarizer!")
    print("Please enter or paste your text below and press Enter twice when done:")

    # Allow user to input multi-line text
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    input_text = " ".join(lines).strip()  # Combine all lines into a single string and strip extra spaces

    if input_text:
        print("\nOriginal Text:\n", input_text)
        summarized_text = summarize_text(input_text)
        print("\nSummarized Text:\n", summarized_text)
    else:
        print("No input provided. Please try again!")
