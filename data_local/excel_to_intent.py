from ChatBot_v1.actions.db_excel import read_excel_file


def nlu(list_ws):
    f = open("nlu.txt", "w", encoding="utf-8")
    f.write('version: "2.0"')
    f.write('\n\nnlu:')
    for i in list_ws:
        max_row = i.max_row
        for j in range(6, max_row + 1):
            intent = i.cell(row=j, column=3).value
            question = i.cell(row=j, column=4).value
            if intent is not None:
                f.writelines(["\n- intent: " + str(intent), "\n  examples: |", "\n    - " + str(question) + '\n'])
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
    list_work_sheet = read_excel_file()
    nlu(list_work_sheet)
    domain(list_work_sheet)
    stories(list_work_sheet)
