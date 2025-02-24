def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8", newline="")
    file.write("제목,회사,보상금,링크")

    for job in jobs:
        file.write(
            f"\n{job[ 'title' ]},{job[ 'company' ]},{job[ 'reward' ]},{job[ 'link' ]}"
        )
    file.close()