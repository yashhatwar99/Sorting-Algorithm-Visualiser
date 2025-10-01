# here we created functions as many as we can
#here both sleection and insertion sort are stable as < it is used not <=


# ┬┌┬┐┌─┐┌─┐┬─┐┌┬┐
# ││││├─┘│ │├┬┘ │
# ┴┴ ┴┴  └─┘┴└─ ┴
import pygame
import random
pygame.init()
clock=pygame.time.Clock()
# input
n=100
list=[]


# ┌─┐┌─┐┬  ┌─┐┬ ┬┬─┐┌─┐
# │  │ ││  │ ││ │├┬┘└─┐
# └─┘└─┘┴─┘└─┘└─┘┴└─└─┘
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

# ┬┌┐┌┌─┐┬ ┬┌┬┐  ┌┐ ┌─┐─┐ ┬
# ││││├─┘│ │ │   ├┴┐│ │┌┴┬┘
# ┴┘└┘┴  └─┘ ┴   └─┘└─┘┴ └─
input_box=pygame.Rect(30,30,100,30)#defined input rectangle

user_input=""
input_on_colour=black
input_off_colour=grey
colour=input_off_colour
input_on=False
input_written=""


# ┌─┐┌─┐┬─┐┌─┐┌─┐┌┐┌  ┬┌┐┌┌─┐┌─┐
# └─┐│  ├┬┘├┤ ├┤ │││  ││││├┤ │ │
# └─┘└─┘┴└─└─┘└─┘┘└┘  ┴┘└┘└  └─┘
width=1000
height=700

# display
screen=pygame.display.set_mode((width,height))




# ┌─┐┌┬┐┬ ┬┌─┐┬─┐  ┬┌┐┌┌─┐┌─┐
# │ │ │ ├─┤├┤ ├┬┘  ││││├┤ │ │
# └─┘ ┴ ┴ ┴└─┘┴└─  ┴┘└┘└  └─┘
speed=1000 #maybe it is the max






# ┌┐ ┌─┐┬─┐  ┬┌┐┌┌─┐┌─┐
# ├┴┐├─┤├┬┘  ││││├┤ │ │
# └─┘┴ ┴┴└─  ┴┘└┘└  └─┘
bar_x=100
bar_y=100
bar_width=(width-2*(100))/n
bar_height=500
height_base=550

# ronadom input
for number in range(n):
    list.append(random.randint(1,100))





# ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌
# ├┤ │ │││││   │ ││ ││││
# └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘


def print_screen():
    screen.fill(white)
    Make_Bars_From_List() #above both function just updated data internally below function will print that on screen
    pygame.display.update()# after each iterstion update karo list ko aur print kro
    event_in_main_loop()  #check which key pressed for responsive action
    clock.tick(speed)


def Bubble_Sort():
    global on
    for bub_var1 in range(n-1):
        if on==False:
            break
        for bub_var2 in range(n-1-bub_var1):
            if on == False:
                break
            if list[bub_var2]>list[bub_var2+1]:
                temp =list[bub_var2]
                list[bub_var2]=list[bub_var2+1]
                list[bub_var2+1]=temp


                # to end
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        on = False
                print_screen()


    return None
def Selection_Sort():
    global on
    for sel_var_1 in range(n-1):
        if on==False:
            break
        sel_min=list[sel_var_1]
        sel_min_ind=sel_var_1
        for sel_var_2 in range(sel_var_1,n):
            if on == False:
                break
            if list[sel_var_2]<sel_min:
                sel_min=list[sel_var_2]
                sel_min_ind=sel_var_2
        temp=list[sel_var_1]
        list[sel_var_1]=list[sel_min_ind]
        list[sel_min_ind]=temp

        # to end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        print_screen()
    return None


def Insertion_Sort():
    global on
    for in_var_1 in range(1,n):
        if on==False:
            break
        for in_var_2 in range(in_var_1,0,-1):#ulta dekhte hue jayenge kaha pr place krna hai
            if on == False:
                break  #so it will end
            if list[in_var_2]<list[in_var_2-1]:
                temp=list[in_var_2]
                list[in_var_2]=list[in_var_2-1]
                list[in_var_2-1]=temp

            #if condition follow ho ya na ho screen update hona chahiye

            # to end
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on = False

            print_screen()
    return None


def Merge(s1,e1,s2,e2):
    global on
    templist=[]
    for i in range(n):
        if on==False:
            break
        templist.append(0)
    # print(templist[0])
    i=s1
    j=s2
    k=s1
    # print(list[j])
    # print(templist[k])
    while i<=e1 and j<=e2: #until one of the list end
        if list[i] <= list[j]:
            # print(templist[k])
            templist[k]=list[i]
            k=k+1
            i=i+1
        else:
            templist[k]=list[j]
            k=k+1
            j=j+1

    #for remaining elements
    if i==s2:#if first list end
        for z in range(j,e2+1):
            templist[k]=list[z]
            k=k+1
    if j==e2+1:
        for z in range(i,e1+1):
            templist[k]=list[z]
            k=k+1


    #now update original list from this
    for z in range(s1,e2+1):
        if on==False:
            break
        list[z]=templist[z]

        # to end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False


        print_screen()


    templist=None  #to free up space delete the list / assign same variable to other and memory space used by list will be cleared by python garbage collector
    return s1,e2


def Divide(s,e):
    mid=(s+e)//2

    if s==e:
        return s,e
    s1,e1=Divide(s,mid)
    s2,e2=Divide(mid+1,e)
    s3,e3=Merge(s1,e1,s2,e2)
    return s3,e3



def Merge_Sort(): #here we are doing without in place algorithm so that it can run faster
    s=0
    e=len(list)-1
    start,end=Divide(s,e)
    return None
    #what actually we did here is
    # we created a empty list at start of each Merge function make it correct
    # then according to it update the original list after each merge function


def partition(s,e):
    global on
    pivot=list[s]
    i=s
    j=e
    while i<j and j>s:
        if on==False:
            break
        while list[i]<=pivot and i<e:
            if on == False:
                break
            i=i+1
        while list[j]>pivot and j>s:
            if on == False:
                break
            j=j-1
        if i<j:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

    temp2=list[j]
    list[j]=list[s]
    list[s]=temp2

    # to end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    print_screen()

    return j






def quick(s,e):
    if s>=e:
        return
    p=partition(s,e)
    quick(s,p-1)
    quick(p+1,e)

def print_text(style,size,to_print,colour,x,y):
    my_font=pygame.font.Font(style,size)
    my_text=my_font.render(to_print,True,colour)
    screen.blit(my_text,(x,y))

def Quick_Sort():
    s=0
    e=len(list)-1
    quick(s,e)

def event_in_main_loop():
    global on
    global bar_width
    global list
    global shown
    global input_on
    global input_written
    global n
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            on=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):  #here event.pos give x.y where mouse button down event occured
                input_on=True
            else:
                input_on=False

        if event.type==pygame.KEYDOWN:#elif so that if quit ho gya to yeh koi kaam na krne lage
            if input_on==True:
                if event.key==pygame.K_RETURN:
                    n=int(input_written)
                    # print("user input",user_input)
                    input_written=""
                    input_on=False
                    shown=2  # so that 2nd time it shows actual n and 1st time it will show default n that is 100

                    # here we reset the list as after inputting new nuber list should update
                    list=[]
                    for number in range(n):
                        list.append(random.randint(1, 100))
                    bar_width = (width - 2 * (100)) / n



                elif event.key==pygame.K_BACKSPACE:
                    input_written=input_written[:-1]

                else:
                    if event.unicode.isdigit():
                        input_written=input_written+event.unicode


            if event.key==pygame.K_b:
                Bubble_Sort()
            if event.key==pygame.K_s:
                Selection_Sort()
            if event.key==pygame.K_i:
                Insertion_Sort()
            if event.key==pygame.K_m:
                Merge_Sort()
            if event.key==pygame.K_q:
                Quick_Sort()


def Make_Bars_From_List(): #since every variablr is global variable in python you can use it inside a function without taking it is input in function
    for i in range(n):
        var=(list[i]*255)/100
        new_colour=(var,0,0)
        pygame.draw.rect(screen,new_colour,(bar_x+i*(bar_width),(bar_y+height_base-((bar_height*list[i])/100)),bar_width,(bar_height*list[i])/100))

def basic_input_box():
    input_on = False
    input_written = ""

# ┬  ┌─┐┌─┐┌─┐
# │  │ ││ │├─┘
# ┴─┘└─┘└─┘┴
shown=1
on=True
while on:
    event_in_main_loop()

    screen.fill(white)

    print_text(None,30,"b-bubble sort  s-selection sort   i-insertion sort  m-merge sort  q-quick sort",red,0,0)
    if shown==1:
        print_text(None,20,"default n=100",black,10,60)

    else:
        print_text(None,20,"n= "+str(n),black,10,60)
        n=int(n)

    # list=[]
    # for number in range(n):
    #     list.append(random.randint(1, 100))
    # bar_width = (width - 2 * (100)) / n
    Make_Bars_From_List()



    pygame.draw.rect(screen, grey, input_box,2,3)   #since i only want to print it on main screen thats why i have not included this line in print_screen function
    print_text(None,25,input_written,black,32,32)
    if input_written=="":
        print_text(None, 25, "Enter Input", black, 32, 32)
    pygame.display.update()

pygame.quit()