import SignupPomorska
import SignupCzajkowski
from multiprocessing import Process
import time


if __name__ == "__main__":
    # Create processes and assign a function for each process
    sp = Process(target=SignupPomorska.signup)
    sc = Process(target=SignupCzajkowski.signup)

    # Start all processes
    sp.start()
    time.sleep(5)
    sc.start()

    # Wait for all processes to finish
    # Block the main program till processes are finished
    sp.join()
    sc.join()

    print("End main")



