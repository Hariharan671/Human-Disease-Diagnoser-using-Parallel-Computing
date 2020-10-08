import os,warnings
warnings.filterwarnings("ignore")
while(1):
    print("\n*******************************************************")
    print("************HUMAN DISEASE PREDICTION SYSTEM************")
    print("*******************************************************\n")
    x=int(input("""Select the Disease for which you want to make prediction :
                   0. Breast Cancer Tumour
                   1. Lung Cancer
                   2. Heart Disease
                   3. Liver Disease
                   4. Diabetes in Females
                   5. Exit\n"""))

    if(x==0):
        os.system('python breastcancer.py')
    elif(x==1):
        os.system('python lung.py')
    elif(x==2):
        os.system('python heart.py')
    elif(x==3):
        os.system('python liver.py')
    elif(x==4):
        os.system('python diabetes.py')
    elif(x==5):
        break;
    else:
        print("INVALID CHOICE :( TRY AGAIN")
    
    
    
