student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score=sum(student_scores)
print(total_score)
print(max(student_scores))
print(min(student_scores))

maxn=0
for i in student_scores:
    if maxn < i:
        maxn = i
print(maxn)





#
# max=0
#
# for score in student_scores:
#     if score > max:
#         max=score
# print(max)
