import csv
import os


def make_report_about_top3(avg_scrs):
    sorted_avg_scrs = {k: v for k, v in sorted(avg_scrs.items(), key=lambda x: x[1], reverse=True)}
    path_to_file = os.path.join(os.getcwd(), 'top3.csv')
    with open(path_to_file, 'w') as csvf:
        writer = csv.writer(csvf, dialect='excel')
        for i, item in enumerate(sorted_avg_scrs.items()):
            if i >= 3:
                break
            writer.writerow([item[0], item[1]])
    return path_to_file


if __name__ == "__main__":
    students_avg_scores = {'Max': 4.999, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}
    print(make_report_about_top3(students_avg_scores))
    
