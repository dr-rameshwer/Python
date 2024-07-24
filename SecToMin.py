print("Enter amount of seconds -");
seconds = eval(input());
minutes = seconds // 60;
second = seconds % 60;

print("There are ", minutes, " and ", second, " in ", seconds, " seconds.")