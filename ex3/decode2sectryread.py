import decode2sectry

if os.path.isfile(source_file):
    decoded_content = read_encoded_file(source_file)
    save_content_to_file(target_file, decoded_content)
else:
    print("Invalid source file")
