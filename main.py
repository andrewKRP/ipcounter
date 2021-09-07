from tkinter import *
from tkinter import messagebox


def clear():
    ip_entry.delete(0, END)
    mask_entry.delete(0, END)
    ip_set.delete(0, END)
    host.delete(0, END)


def network_show():
    flag = False
    network_address = []
    ip = ip_entry.get().split('.')
    mask = mask_entry.get().split('.')
    for i in range(len(ip)):
        ip[i] = int(ip[i])
        mask[i] = int(mask[i])

    for i in range(len(ip)):
        if 0 <= ip[i] <= 255 and 0 <= mask[i] <= 255:
            network_address.append(str(int(bin(ip[i] & mask[i])[2:], 2)))
        else:
            messagebox.showinfo("IP counter", "Incorrect ip or mask")
            clear()
            flag = True
            break

    if not flag:
        ip_set.insert(0, '.'.join(network_address))
        try:
            mount_of_hosts()
        except KeyError:
            messagebox.showinfo("IP counter", "Incorrect mask")
            clear()


def mount_of_hosts():
    mask_dic = {'255.255.255.255': '1', '255.255.255.254': '2',
                '255.255.255.252': '2', '255.255.255.248': '6',
                '255.255.255.240': '14', '255.255.255.224': '30',
                '255.255.255.192': '62', '255.255.255.128': '126',
                '255.255.255.0': '254', '255.255.254.0': '510',
                '255.255.252.0': '1022', '255.255.248.0': '2046',
                '255.255.240.0': '4094', '255.255.224.0': '8190',
                '255.255.192.0': '16382', '255.255.128.0': '32766',
                '255.255.0.0': '65534', '255.254.0.0': '131070',
                '255.252.0.0': '262142', '255.248.0.0': '524286',
                '255.240.0.0': '1048574', '255.224.0.0': '2097150',
                '255.192.0.0': '4194302', '255.128.0.0': '8388606',
                '255.0.0.0': '16777214', '254.0.0.0': '33554430',
                '252.0.0.0': '67108862', '248.0.0.0': '134217726',
                '240.0.0.0': '268435454', '224.0.0.0': '536870910',
                '192.0.0.0': '1073741822', '128.0.0.0': '2147483646',
                '0.0.0.0': '4294967294'}

    host.insert(0, mask_dic[mask_entry.get()])


root = Tk()
root.attributes('-alpha', 1)
root.title("IP counter")
root.geometry('400x400')

ip_label = Label(text="Enter your IPv4-address(ex:192.168.0.1):")
ip_label.place(x=5, y=50)

mask_label = Label(text="Enter your network mask(ex:255.255.255.0):")
mask_label.place(x=5, y=100)

ip_entry = Entry()
ip_entry.place(x=240, y=50)

mask_entry = Entry()
mask_entry.place(x=240, y=100)

ip_set = Entry()
ip_set.place(x=240, y=150)

ip_set_label = Label(text="Here your network-address(ex:192.168.0.0):")
ip_set_label.place(x=5, y=150)

host = Entry()
host.place(x=240, y=200)

host_label = Label(text="Max number of hosts: ")
host_label.place(x=5, y=200)

exit_button = Button(text='Exit', command=root.destroy)
exit_button.place(x=315, y=370, width=80)

calculate_button = Button(text='Calculate', command=network_show)
calculate_button.place(x=230, y=370, width=80)

clear_button = Button(text='Clear', command=clear)
clear_button.place(x=145, y=370, width=80)

root.mainloop()
