#############################################
# Print integers 1 to 10 without using a loop
#############################################
print(1)
print(2)
print(3)

print(1:10)
cat(1:10)

######################################
# Print integers 1 to 10 using a loop
######################################
for (i in c(1:10)){
  print(i)
}

for (i in c(1:10)){
  cat(i, "")
}

j <- 1
while (j <= 10){
  print(j)
  j <- j + 1
}