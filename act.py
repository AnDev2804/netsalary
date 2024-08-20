import csv
import tkinter as tk
def sneto(sex,tip,ant,car,sd):
    if sex == 'F':
        sn=float(sd)+(float(sd)*((int(ant)/3)*0.02))
        
        sn=sn+((float(sd)*0.15)+float(sd))
        
        if tip == 'C':
            sn=sn+(float(sd)*0.1)
            
        elif tip == 'F':
            sn=sn+(float(sd)*0.2)
            
        else:
            sn=sn+100
            
        if car == '1':
            sn=sn+1500
            
        elif car == '2':
            sn=sn+1200
            
        elif car == '3':
            sn=sn+1000
            
        elif car == '4':
            sn=sn+800
            
        elif car == '5':
            sn=sn+500
        return sn
    else:
        sn=float(sd)+(float(sd)*((int(ant)/3)*0.02))
        sn=(float(sd)*0.1)+float(sd)
        if tip == 'C':
            sn=sn+(float(sd)*0.1)
            
        elif tip == 'F':
            sn=sn+(float(sd)*0.2)
            
        else:
            sn=sn+100
            
        if car == '1':
            sn=sn+1500
            
        elif car == '2':
            sn=sn+1200
            
        elif car == '3':
            sn=sn+1000
            
        elif car == '4':
            sn=sn+800
            
        elif car == '5':
            sn=sn+500
        return sn
def mostrar(ci):

    with open ("PY_EMPLEADOS.csv",newline='') as arch:
        l=csv.reader(arch,delimiter=';')
        for row in l:
            if row[0] == ci:
                sex_label=tk.Label(root,text="Sexo:")
                sex_label.pack(pady=5)
                sex=tk.StringVar()
                sex.set(row[1])
                sex_entry=tk.Entry(root,textvariable=sex)
                sex_entry.pack(pady=5)
                sexo=row[1]
                    
                fnac_label=tk.Label(root,text="Fecha de Nacimiento:")
                fnac_label.pack(pady=5)
                fnac=tk.StringVar()
                fnac.set(row[2])
                fnac_entry=tk.Entry(root,textvariable=fnac)
                fnac_entry.pack(pady=5)

                n1_label=tk.Label(root,text="Primer Nombre:")
                n1_label.pack(pady=5)
                n1=tk.StringVar()
                n1.set(row[3])
                n1_entry=tk.Entry(root,textvariable=n1)
                n1_entry.pack(pady=5)

                n2_label=tk.Label(root,text="Segundo Nombre:")
                n2_label.pack(pady=5)
                n2=tk.StringVar()
                n2.set(row[4])
                n2_entry=tk.Entry(root,textvariable=n2)
                n2_entry.pack(pady=5)

                a1_label=tk.Label(root,text="Primer Apellido:")
                a1_label.pack(pady=5)
                a1=tk.StringVar()
                a1.set(row[5])
                a1_entry=tk.Entry(root,textvariable=a1)
                a1_entry.pack(pady=5)

                a2_label=tk.Label(root,text="Segundo Apellido:")
                a2_label.pack(pady=5)
                a2=tk.StringVar()
                a2.set(row[6])
                a2_entry=tk.Entry(root,textvariable=a2)
                a2_entry.pack(pady=5)
    with open("PY_LABORAL.csv",newline='') as arch2:
            l2=csv.reader(arch2,delimiter=';')
            for row in l2:
                if row[0] == ci:
                    tipo_label=tk.Label(root,text="Tipo:")
                    tipo_label.pack(pady=5)
                    tipo=tk.StringVar()
                    tipo.set(row[1])
                    tipo_entry=tk.Entry(root,textvariable=tipo)
                    tipo_entry.pack(pady=5)
                    tp=row[1]

                    ant_label=tk.Label(root,text="Antiguedad:")
                    ant_label.pack(pady=5)
                    ant=tk.StringVar()
                    ant.set(row[2])
                    ant_entry=tk.Entry(root,textvariable=ant)
                    ant_entry.pack(pady=5)
                    antg=row[2]

                    car_label=tk.Label(root,text="Cargo:")
                    car_label.pack(pady=5)
                    car=tk.StringVar()
                    car.set(row[3])
                    car_entry=tk.Entry(root,textvariable=car)
                    car_entry.pack(pady=5)
                    carg=row[3]

                    sd_label=tk.Label(root,text="Sueldo Base:")
                    sd_label.pack(pady=5)
                    sd=tk.StringVar()
                    sd.set(row[4])
                    sd_entry=tk.Entry(root,textvariable=sd)
                    sd_entry.pack(pady=5)
                    sb=row[4]
    sn=sneto(sexo,tp,antg,carg,sb)
    sn_label=tk.Label(root,text="Sueldo Neto:")
    sn_label.pack(pady=5)
    snf=tk.StringVar()
    snf.set(sn)
    sn_entry=tk.Entry(root,textvariable=snf)
    sn_entry.pack(pady=5)
    input_frame = tk.Frame(root)
    input_frame.pack(pady=5)
    ci_label = tk.Label(input_frame, text="Cedula:")
    ci_label.pack(side="left")
    ci_entry = tk.Entry(input_frame)
    ci_entry.pack(side="left")
    consultar = tk.Button(input_frame, text="Consultar", command=lambda: submit(ci_entry))
    consultar.pack(side="left")
    def submit(ci_entry):
        ci = ci_entry.get()
        input_frame.destroy()
        for widget in root.winfo_children():
            widget.destroy()
        dat = mostrar(ci)
root=tk.Tk()
root.title("Consulta de datos")
root.geometry("600x1000")
#formulario
#----------------------------------------------------------------
input_frame = tk.Frame(root)
input_frame.pack(pady=5)
ci_label = tk.Label(input_frame, text="Cedula:")
ci_label.pack(side="left")
ci_entry = tk.Entry(input_frame)
ci_entry.pack(side="left")
consultar = tk.Button(input_frame, text="Consultar", command=lambda: submit(ci_entry))
consultar.pack(side="left")
def submit(ci_entry):
    ci = ci_entry.get()
    input_frame.destroy()
    for widget in root.winfo_children():
        widget.destroy()
    dat = mostrar(ci)

root.mainloop()
