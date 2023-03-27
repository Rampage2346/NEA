# import pyttsx3
# engine = pyttsx3.init()
# engine.say("wee woo")
# engine.runAndWait()
# from MainAPICall import allPlayerData
#
#
# def all_data(name, id):
#     global mmr_history
#     all_dicts = allPlayerData(name, id)
#     mmr_history = all_dicts[2]
#
#
# # [30, 19, -18]
# def format_rr(rr):
#     main = []
#     negative = False
#     str_rr = []
#     for i in range(0, len(rr)):
#         print(i)
#         temp = str(rr[i])
#         print(temp)
#         str_rr.append(temp)
#
#     print(str_rr)
#     for x in range(0, len(str_rr)):
#         split = [*(str_rr[x])]
#
#         if split[0] != "-":
#             split.insert(0, "+")
#             appended_item = "".join(split)
#             main.append(appended_item)
#         else:
#             appended_item = "".join(split)
#             main.append(appended_item)
#
#         print(split)
#         print(main)
#     return main

#
#     for y in range(0, len(split)):
#         if split == "-":
#             negative = True
#         else:
#             negative = False
#     if negative == False:
#         split.insert(0, "+")
# print(rr)

# for i in range(0, len(rr)):
#     temp = str(rr[i])
#     rr.insert(i, temp)
#     print(temp)
#     split = [*temp]
#     negative = False
#     for a in range(0, len(split)):
#         if split == "-":
#             negative = True
#     if negative == False:
#         rr.insert(0, "+")
#     print(rr)


# if __name__ == '__main__':
#     all_data("Amaz", "4510")
#
#     mmr1 = mmr_history[1]["mmr_change"][0]
#     mmr2 = mmr_history[2]["mmr_change"][0]
#     mmr3 = mmr_history[3]["mmr_change"][0]
#
#     rr = []
#     rr.append(mmr1)
#     rr.append(mmr2)
#     rr.append(mmr3)
#
#     format_rr(rr)
