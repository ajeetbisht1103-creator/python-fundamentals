# ----------------------------------------------------
# Description:
# This program converts a given duration
# in seconds into hours, minutes, and seconds.
# ----------------------------------------------------

total_seconds = int(input("Enter time in seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")