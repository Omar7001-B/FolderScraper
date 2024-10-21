import os

def scrape_directory_content(directory_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Walk through all directories and files
        for root, dirs, files in os.walk(directory_path):
            output_file.write(f"Directory: {root}\n")
            output_file.write('-' * 50 + '\n')

            # Loop through the files in the current directory
            for file_name in files:
                file_path = os.path.join(root, file_name)
                output_file.write(f"File: {file_name}\n")
                output_file.write('-' * 50 + '\n')

                try:
                    # Open each file and write its content
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        output_file.write(content)
                        output_file.write('\n' + '=' * 50 + '\n')
                except Exception as e:
                    # Handle any errors (e.g., unreadable files)
                    output_file.write(f"Could not read file {file_name}: {e}\n")
                    output_file.write('\n' + '=' * 50 + '\n')

if __name__ == "__main__":
    directory_path = r"E:\Learning\Projects\Cobweb Mod\cobweb-template-1.20\src\main\java\com\example"  # Replace with your directory
    output_file_path = "output.txt"  # Output file to store the scraped content
    scrape_directory_content(directory_path, output_file_path)
    print(f"Scraping complete. Data has been written to {output_file_path}")
