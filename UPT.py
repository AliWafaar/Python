#Loop Utama
while True:
    try:
    #User Input
        jumlah_item= (input('Masukkan Jumlah Item EOD di pisahkan dengan koma:'))
        element_item= jumlah_item.split(",")
        item_bersih= [int(item) for item in element_item]
        total_item= sum(item_bersih)
    
        jumlah_trx= (input('Masukkan Jumlah Transaksi EOD di pisahkan dengan koma:'))
        element_trx= jumlah_trx.split(',')
        trx_bersih= [int(trx)for trx in element_trx]
        total_trx= sum(trx_bersih)

        upt_target= int(input('Masukkan Target UPT Anda:'))
    
    #Rumus Utama
        if len(element_item)==len(element_trx):
            upt= (total_item / total_trx)
            if upt <= upt_target :
                print (f'Data dari {len(element_item)} Hari Adalah:\n{total_trx} Transaksi Dan {total_item} Item\nUPT anda {upt} Masih Di Bawah {upt_target} Mohon Di Tingkatkan')
            else :
                print (f'Data dari {len(element_item)} Hari Adalah:\n{total_trx} Transaksi Dan {total_item} Item\nUPT anda {upt} Sudah Di Atas {upt_target} Mohon Di Pertahankan')
        
            while True:
                report_kembali=input('apakah anda mau melakukan report kembali (y/n):')
                if report_kembali.lower()=='y':
                    break
                elif report_kembali.lower()=='n':
                    print('Terimakasih Semoga Bisnis Anda Lancar!')
                    exit()
                else:
                    print('Input Hanya Dengan Huruf (Y/N)')
        
        

    #Input User Salah
        else:
            print ('Jumlah Data Item dan Transaksi Harus Sama ')
            continue
    except ValueError:
        print('Masukkan Data Hanya dengan Angka dan Koma (,)')
