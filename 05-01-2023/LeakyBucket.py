import random
import time

BUFFER_SIZE = 500
EXIT_RATE = 250
BUFFER_QUEUE = []

def LB(packet_size,BUFFER_SIZE,BUFFER_QUEUE):
    if (packet_size + sum(BUFFER_QUEUE) > BUFFER_SIZE):
        return False
    return True


def main():
    while True:
        generate_datapacket = random.randint(1,650)
        print("Data packet size generated:{}".format(generate_datapacket))
        if LB(generate_datapacket,BUFFER_SIZE,BUFFER_QUEUE):
            BUFFER_QUEUE.insert(0,generate_datapacket)
            print("Buffer State :{}  Total filled:{}".format(BUFFER_QUEUE,sum(BUFFER_QUEUE)))
            time.sleep(2)
            try:
                BUFFER_QUEUE[-1] = BUFFER_QUEUE[-1] - EXIT_RATE
                if BUFFER_QUEUE[-1] < 0:
                    temp = abs(BUFFER_QUEUE[-1])
                    BUFFER_QUEUE.pop()
                    try:
                        BUFFER_QUEUE[-1] -= BUFFER_QUEUE[-1]-temp
                    except Exception:
                        continue
            except Exception:
                continue

        else:
            print("Overflow")
            time.sleep(2)
            try:
                BUFFER_QUEUE[-1] = BUFFER_QUEUE[-1] - EXIT_RATE
                if BUFFER_QUEUE[-1] < 0:
                    temp = abs(BUFFER_QUEUE[-1])
                    BUFFER_QUEUE.pop()
                    try:
                        BUFFER_QUEUE[-1] -= BUFFER_QUEUE[-1]-temp
                    except Exception:
                        continue
            except Exception:
                continue

main()