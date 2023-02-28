import divideConquer as dc 
import bruteForce as bf
import visualize as vs
import platform
import time
import os
def splashScreen(): 
    print (" ______     __         ______     ______     ______     ______     ______      ______   ______     __     ______    ")    
    print ("/\  ___\   /\ \       /\  __ \   /\  ___\   /\  ___\   /\  ___\   /\__  _\    /\  == \ /\  __ \   /\ \   /\  == \   ")
    print ("\ \ \____  \ \ \____  \ \ \/\ \  \ \___  \  \ \  __\   \ \___  \  \/_/\ \/    \ \  _-/ \ \  __ \  \ \ \  \ \  __<   ")
    print (" \ \_____\  \ \_____\  \ \_____\  \/\_____\  \ \_____\  \/\_____\    \ \_\     \ \_\    \ \_\ \_\  \ \_\  \ \_\ \_\ ")
    print ("  \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/     \/_/      \/_/     \/_/\/_/   \/_/   \/_/ /_/ ")
    print ("                                                                                                                    ")      
                                                                                                                    
def main():
    splashScreen()
    n = int(input("Masukkan jumlah titik: "))
    m = int(input("Masukkan jumlah dimensi: "))
    while(n < 2):
        n = int(input("Masukkan jumlah titik: "))
        m = int(input("Masukkan jumlah dimensi: "))

    points = dc.generate_points(n, m)    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================================================")
    print("                 Divide & Conquer Algorithm                 ")
    print("============================================================")
    startTime1 = time.time()
    p, q, d = dc.closest_pair(points)
    endTime1 = time.time()
    totalTime1 = (endTime1 - startTime1)*1000
    print("Waktu eksekusi divide and conquer: {:.3f}".format(totalTime1), "ms")
    print("Jumlah operasi euclidean: ", dc.counterEuclidean)
    print("Jarak terdekat: {:.3f}".format(d))
    print("Platform: ", platform.processor())
    print("===========================================================")
    print("                   Brute Force Algorithm                   ")
    print("===========================================================")

    startTime2 = time.time()
    p1, q1, d1 = bf.closest_pair_bf(points)
    endTime2 = time.time()
    totalTime2 = (endTime2 - startTime2)*1000
    print("Waktu eksekusi brute force: {:.3f}".format(totalTime2), "ms")
    print("Jumlah operasi euclidean brute force: ", dc.counterEuclidean)
    print("Platform: ", platform.processor())
    print("Jarak terdekat: {:.3f}".format(d1))
    print("============================================================")
    print("Apakah anda yakin ingin melihat visualisasi? (y/n)")
    answer = input()
    if(answer == 'y'):
        if m == 1:
            vs.visualize_closest_pair1(points)
        elif m == 2:
            vs.visualize_closest_pair2(points)
        elif m == 3:
            vs.visualize_closest_pair3(points)
        else:
            print("Maaf, visualisasi hanya tersedia untuk 1, 2, dan 3 dimensi")
        print("Apakah anda ingin mengulang permainan? (y/n)")
        if input() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            
            print("Terima kasih telah menggunakan program kami!")
    else:
        print("Apakah anda ingin mengulang permainan? (y/n)")
        if input() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            
            print("Terima kasih telah menggunakan program kami!")
            
main()