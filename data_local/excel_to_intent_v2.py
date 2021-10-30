from ChatBot_v1.actions.db_excel import read_excel_file, file_name_question


def nlu(list_ws):
    f = open("nlu.txt", "w", encoding="utf-8")
    f.write('version: "2.0"')
    f.write('\n\nnlu:')
    for i in list_ws:
        max_row = i.max_row
        max_col = i.max_column
        for j in range(2, max_col + 1):
            intent = i.cell(row=1, column=j).value
            f.writelines(["\n- intent: " + str(intent), "\n  examples: |"])
            for k in range(2, max_row + 1):
                question = i.cell(row=k, column=j).value
                print(question)
                if question is not None:
                    f.write("\n    - " + str(question))
                else:
                    break
            f.write("\n")
    f.close()


def domain(list_ws):
    f = open("domain.txt", "w", encoding="utf-8")
    for i in list_ws:
        max_row = i.max_row
        for j in range(6, max_row + 1):
            intent = i.cell(row=j, column=3).value
            if intent is not None:
                f.write("  - " + str(intent) + "\n")
    f.close()


def stories(list_ws):
    f = open("stories.txt", "w", encoding="utf-8")
    f.write("- story: bot return message\n")
    f.write("  steps:")
    for i in list_ws:
        max_row = i.max_row
        for j in range(6, max_row + 1):
            intent = i.cell(row=j, column=3).value
            if intent is not None:
                f.writelines(["\n  - intent: " + str(intent), "\n  - action: action_bot_answer"])
    f.close()


if __name__ == "__main__":
    list_work_sheet = read_excel_file(file_name=file_name_question)
    list_work_sheet2 = read_excel_file()
    nlu(list_work_sheet)
    domain(list_work_sheet2)
    stories(list_work_sheet2)
