import os

<<<<<<< HEAD

=======
>>>>>>> 711dc27144f25bd2a19c2bc37957622fcb52c43f
path = "." 
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])