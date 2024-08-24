from commands.get_data_register import info
from commands.get_data_login import login
from commands.get_data_product import Add_product
from commands.get_data_password import change_pass , change_pass2
from controller.action import do
def show(u):
    status = True
    while status:
        m = input("1.Products\n2.Categories\n3.My product\n4.Add product\n5.Account Information\n6.Logout\n")
        if m == "1":
            while True:
                f = input("1.All Product\n2.Search\n3.Exit\n")
                if f == "1":
                    do(u).view()
                    n = input("please inter the productiId: ")
                    do(u).choosee(n)
                    status = False
                    while True:
                        r = input("1.like\n2.buy\n4.exit\n")
                        if r == "1":
                            do(u).likee(n)
                        elif r == "2":
                            pass
                        elif r == "3":
                            status = True
                            break
                        else:
                            print("wrong choiced1❌")
                elif f == "2":
                    nameproduct = input("Search: ")
                    do(u).searchh(nameproduct)
                    n = input("please inter the productiId: ")
                    while True:
                        r = input("1.like\n2.buy\n3.exit\n")
                        if r == "1":
                            do(u).likee(n)
                        elif r == "2":
                            pass
                        elif r == "3":
                            break
                        else:
                            print("wrong choiced234❌")
                elif f == "3":
                    break
                else:
                    print("wrong choiced4❌")        
        elif m == "2":
            category_list = ["Car","Electronics","Food","Toys","Beauty","Home","Fitness","Petproducts","designed","PersonalCare","Fashion"]
            mohs = True
            while mohs:
                e = int(input("1.Car\n2.Electronics\n3.Food\n4.Toys\n5.Beauty\n6.Home\n7.Fitness\n8.NextPage\n9.Exit\n"))
                if e < 8:
                    x = category_list[(e-1)]
                    do(u).categoryy(x)
                    mohs = False
                    n = input("please inter the productiId: ")
                    do(u).choosee(n)
                    while True:
                        r = input("1.like\n2.buy\n3.exit\n")
                        if r == "1":
                            do(u).likee(n)
                        elif r == "2":
                            pass
                        elif r == "3":
                            mohs = True
                            break
                        else:
                            print("wrong choiced12❌")
                elif e == 8:
                    while True:
                        c = int(input("1.Petproducts\n2.designed\n3.PersonalCare\n4.Fashion\n5.back\n"))
                        if c < 5:
                            x = category_list[(c+6)]
                            do(u).categoryy(x)
                            mohs = False
                            n = input("please inter the productiId: ")
                            do(u).choosee(n)
                            while True:
                                r = input("1.like\n2.buy\n3.exit\n")
                                if r == "1":
                                    do(u).likee(n)
                                elif r == "2":
                                    pass
                                elif r == "3":
                                    break
                                else:
                                    print("wrong choiced11❌")
                            
                        elif c == 5:
                            mohs = True
                            break
                        else:
                            print("wrong choiced9❌")  
                elif e == 9:
                    break
                else:
                    print("wrong choiced10❌") 
        elif m == "3":
            do(u).myproductt()
                
        elif m == "4":
            product_name, product_description, product_price,product_category,image = Add_product()
            do(u).add_product(product_name, product_description, product_price,product_category,image)
        elif m == "5":
            while True:
                f = input("1.Information\n2.update Information\n3.My product\n4.Exit\n")
                if f == "1":
                    do(u).infoo()   
                elif f == "2":
                    p = change_pass()
                    p1,p2 = change_pass2()
                    do(u).change_pass(p,p1,p2)
                elif f == "3":
                    pass
                elif f == "4":
                    break
                
                else:
                    print("wrong choiced5❌")
        elif m == "6":
            break   
        else:
            print("wrong choiced3❌")
