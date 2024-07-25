
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")



    # img=Image.open(path_MS2) # read the image file
    # img=img.resize((497,355)) # new width & height
    # img=ImageTk.PhotoImage(img)
    # e1 =Label(optical_image_frame)
    # e1.pack(side=TOP)
    # e1.image = img # keep a reference! by attaching it to a widget attribute
    # e1['image']=img # Show Image 


window = Tk()

window.geometry("778x883")
window.configure(bg = "#423C56")
window.title('EndoGenius')
# window.iconbitmap(r"LiClaw.ico")



input_path_MS2 = StringVar()
input_path_format_MS2 = StringVar()

mz_range_min = StringVar()
mz_range_max = StringVar()
min_intensity = StringVar()
max_precursor_z = StringVar()
max_fragment_z = StringVar()

database_csv_path = StringVar()
target_peptide_list_path = StringVar()
fasta_path = StringVar()

precursor_err = StringVar()
fragment_err = StringVar()
max_mods_pep = StringVar()
amid_var = IntVar()
ox_var = IntVar()
pgE_var = IntVar()
sulf_var = IntVar()
pgQ_var = IntVar()

motif_db_path = StringVar()
confident_coverage_threshold = StringVar()
standard_err = StringVar()
max_adjacent_swapped_AAs = StringVar()
FDR_threshold = StringVar()
max_swapped_AA = StringVar()

output_dir_path = StringVar()

def openweb_liweb():
    new = 1
    url = "https://www.lilabs.org/resources"
    webbrowser.open(url,new=new)

def openweb_git():
    new = 1
    url = "https://github.com/lingjunli-research"
    webbrowser.open(url,new=new)

def openweb_user_manual():
    new = 1
    url = "https://docs.google.com/document/d/e/2PACX-1vRKyqvEpRbcrYHWTq1CLRImNfC6f_gxaXnKgH2I_ZX_E-kSA2PvUiy4d8kMddS2B8PcEwsLAngMcjvg/pub"
    webbrowser.open(url,new=new)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def raw_MS2_path():
    path_MS2 = askopenfilename(filetypes=[(".MS2 Files",("*.MS2"))]) 
    input_path_MS2.set(path_MS2)

def formatted_MS2_path():
    path_format_MS2 = askopenfilename(filetypes=[("Text Files",("*.txt"))]) 
    input_path_format_MS2.set(path_format_MS2)
    
def prebuilt_db_path():
    path_prebuilt_db = askopenfilename(filetypes=[("CSV Files",("*.csv"))]) 
    database_csv_path.set(path_prebuilt_db)
    
def target_list_path_get():
    path_target_list = askopenfilename(filetypes=[("CSV Files",("*.csv"))]) 
    target_peptide_list_path.set(path_target_list)

def fasta_db_get():
    path_fasta = askopenfilename(filetypes=[("FASTA Files",("*.fasta"))]) 
    fasta_path.set(path_fasta)
    
def motif_db_get():
    path_motif_db = askopenfilename(filetypes=[("CSV Files",("*.csv"))]) 
    motif_db_path.set(path_motif_db)
    
def output_path_get():
    path_out = filedialog.askdirectory() 
    output_dir_path.set(path_out)

def begin_search():
    print('search will begin now')

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Li Lab Website", command=openweb_liweb)
helpmenu.add_command(label="Li Lab GitHub", command=openweb_git)
helpmenu.add_command(label="User manual", command=openweb_user_manual)
menubar.add_cascade(label="Help", menu=helpmenu)

# toolmenu = Menu(menubar, tearoff=0)
# toolmenu.add_command(label="Step evaluate tool")
# menubar.add_cascade(label="Tools", menu=toolmenu)

window.config(menu=menubar)

canvas = Canvas(
    window,
    bg = "#423C56",
    height = 883,
    width = 778,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    10.0,
    200.0,
    773.0,
    257.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    20.0,
    216.0,
    anchor="nw",
    text="m/z range",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    171.0,
    219.0,
    anchor="nw",
    text="-",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    270.0,
    210.0,
    anchor="nw",
    text="minimum\nintensity",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    420.0,
    210.0,
    anchor="nw",
    text="max precursor\ncharge",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    600.0,
    210.0,
    anchor="nw",
    text="max fragment\ncharge",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    5.0,
    166.0,
    anchor="nw",
    text="2. Spectral processing",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    5.0,
    76.0,
    anchor="nw",
    text="1. Spectral input",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    10.0,
    109.0,
    369.0,
    166.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    32.0,
    128.0,
    anchor="nw",
    text="Raw .MS2",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    411.0,
    109.0,
    770.0,
    166.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    600.0,
    138.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=input_path_format_MS2
)

entry_1.place(
    x=527.0,
    y=123.0,
    width=146.0,
    height=28.0
)

canvas.create_text(
    440.0,
    119.0,
    anchor="nw",
    text="Formatted\nRaw .MS2",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    332.0,
    125.0,
    anchor="nw",
    text="or",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    5.0,
    582.0,
    anchor="nw",
    text="5. PSM assignment",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    10.0,
    613.0,
    770.0,
    715.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    14.0,
    626.0,
    anchor="nw",
    text="Motif database",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    425.0,
    626.0,
    anchor="nw",
    text="Confident coverage threshold (%)",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    22.0,
    668.0,
    anchor="nw",
    text="Standard\nerror %",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    180.0,
    668.0,
    anchor="nw",
    text="Max # of adjacent\nswapped AAs",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    5.0,
    720.0,
    anchor="nw",
    text="6. Export results",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    10.0,
    749.0,
    411.0,
    808.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    29.0,
    769.0,
    anchor="nw",
    text="Output directory",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    5.0,
    265.0,
    anchor="nw",
    text="3. Database definition",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    10.0,
    315.0,
    369.0,
    436.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    32.0,
    334.0,
    anchor="nw",
    text="Database",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    21.0,
    388.0,
    anchor="nw",
    text="Target\npeptide list",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    338.0,
    335.0,
    anchor="nw",
    text="or",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    7.0,
    293.0,
    anchor="nw",
    text="Pre-built database",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    420.0,
    293.0,
    anchor="nw",
    text="Generate from .fasta",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    414.0,
    316.0,
    773.0,
    374.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    436.0,
    335.0,
    anchor="nw",
    text="Database",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    10.0,
    466.0,
    773.0,
    579.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    25.0,
    489.0,
    anchor="nw",
    text="Precursor error (ppm)",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    14.0,
    540.0,
    anchor="nw",
    text="Modifications",
    fill="#000000",
    font=("Inter", 16 * -1)
)

amid_check = Checkbutton(canvas, onvalue=1, offvalue=0, variable=amid_var, bg= '#D9D9D9')
amid_check.place(x = 130, y = 538)

canvas.create_text(
    158.0,
    542.0,
    anchor="nw",
    text="C-terminal amidation",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    489.0,
    anchor="nw",
    text="Fragment error (Da)",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    550.0,
    489.0,
    anchor="nw",
    text="Max mods/peptide",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    5.0,
    436.0,
    anchor="nw",
    text="4. Database search",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=begin_search,
    relief="flat"
)
button_1.place(
    x=9.0,
    y=820.0,
    width=401.0,
    height=59.0
)

canvas.create_text(
    5.0,
    0.0,
    anchor="nw",
    text="EndoGenius",
    fill="#FFFFFF",
    font=("Inter", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    617.0,
    799.0,
    image=image_image_1
)

canvas.create_text(
    390.0,
    668.0,
    anchor="nw",
    text="FDR\nThreshold",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

canvas.create_text(
    550.0,
    668.0,
    anchor="nw",
    text="Max # of single\nswapped AAs",
    fill="#000000",
    font=("Inter", 16 * -1),
    justify='center'
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=formatted_MS2_path,
    relief="flat"
)
button_2.place(
    x=678.0,
    y=123.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    204.0,
    138.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable = input_path_MS2
)
entry_2.place(
    x=131.0,
    y=123.0,
    width=146.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=raw_MS2_path,
    relief="flat"
)
button_3.place(
    x=282.0,
    y=123.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    241.0,
    779.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=output_dir_path
)

entry_3.place(
    x=168.0,
    y=764.0,
    width=146.0,
    height=28.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=output_path_get,
    relief="flat"
)
button_4.place(
    x=319.0,
    y=764.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    604.0,
    344.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=fasta_path
)

entry_4.place(
    x=531.0,
    y=329.0,
    width=146.0,
    height=28.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=fasta_db_get,
    relief="flat"
)
button_5.place(
    x=682.0,
    y=329.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    194.0,
    344.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=database_csv_path
)

entry_5.place(
    x=121.0,
    y=329.0,
    width=146.0,
    height=28.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=prebuilt_db_path,
    relief="flat"
)
button_6.place(
    x=272.0,
    y=329.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    194.0,
    403.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_6.insert(END,'entry_6')
entry_6.place(
    x=121.0,
    y=388.0,
    width=146.0,
    height=28.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=272.0,
    y=388.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    194.0,
    403.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=target_peptide_list_path
)

entry_7.place(
    x=121.0,
    y=388.0,
    width=146.0,
    height=28.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=target_list_path_get,
    relief="flat"
)
button_8.place(
    x=272.0,
    y=388.0,
    width=77.21710205078125,
    height=30.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    214.0,
    639.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=motif_db_path
)

entry_8.place(
    x=141.0,
    y=624.0,
    width=146.0,
    height=28.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    127.5,
    685.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=standard_err
)

entry_9.place(
    x=101.0,
    y=670.0,
    width=53.0,
    height=28.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    738.5,
    229.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable = max_fragment_z
)

entry_10.place(
    x=712.0,
    y=214.0,
    width=53.0,
    height=28.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    563.5,
    228.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable = max_precursor_z
)

entry_11.place(
    x=537.0,
    y=213.0,
    width=53.0,
    height=28.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    378.5,
    228.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable = min_intensity
)

entry_12.place(
    x=352.0,
    y=213.0,
    width=53.0,
    height=28.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    222.5,
    228.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=mz_range_max
)

entry_13.place(
    x=196.0,
    y=213.0,
    width=53.0,
    height=28.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    132.5,
    228.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable= mz_range_min
)

entry_14.place(
    x=106.0,
    y=213.0,
    width=53.0,
    height=28.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    711.5,
    498.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable= max_mods_pep
)

entry_15.place(
    x=685.0,
    y=483.0,
    width=53.0,
    height=28.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    465.5,
    498.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=fragment_err
)

entry_16.place(
    x=439.0,
    y=483.0,
    width=53.0,
    height=28.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    215.5,
    498.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=precursor_err
)

entry_17.place(
    x=189.0,
    y=483.0,
    width=53.0,
    height=28.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    711.5,
    636.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=confident_coverage_threshold
)

entry_18.place(
    x=685.0,
    y=621.0,
    width=53.0,
    height=28.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    344.5,
    684.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=max_adjacent_swapped_AAs
)

entry_19.place(
    x=318.0,
    y=669.0,
    width=53.0,
    height=28.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    498.5,
    684.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=FDR_threshold
)

entry_20.place(
    x=472.0,
    y=669.0,
    width=53.0,
    height=28.0
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    711.5,
    684.0,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=max_swapped_AA
)

entry_21.place(
    x=685.0,
    y=669.0,
    width=53.0,
    height=28.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=motif_db_get,
    relief="flat"
)
button_9.place(
    x=292.0,
    y=624.0,
    width=77.21710205078125,
    height=30.0
)

canvas.create_rectangle(
    138.0,
    544.0,
    156.0,
    562.0,
    fill="#D9D9D9",
    outline="")

ox_check = Checkbutton(canvas, onvalue=1, offvalue=0, variable=ox_var, bg= '#D9D9D9')
ox_check.place(x = 288, y = 538)

canvas.create_text(
    315.0,
    542.0,
    anchor="nw",
    text="Oxidation of M",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_rectangle(
    295.0,
    544.0,
    313.0,
    562.0,
    fill="#D9D9D9",
    outline="")

pgE_check = Checkbutton(canvas, onvalue=1, offvalue=0, variable=pgE_var, bg= '#D9D9D9')
pgE_check.place(x = 410, y = 538)

canvas.create_text(
    437.0,
    542.0,
    anchor="nw",
    text="Pyro-glu from E",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_rectangle(
    417.0,
    544.0,
    435.0,
    562.0,
    fill="#D9D9D9",
    outline="")

pgQ_check = Checkbutton(canvas, onvalue=1, offvalue=0, variable=pgQ_var, bg= '#D9D9D9')
pgQ_check.place(x = 645, y = 538)


canvas.create_text(
    672.0,
    542.0,
    anchor="nw",
    text="Pyro-glu from Q",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_rectangle(
    652.0,
    544.0,
    670.0,
    562.0,
    fill="#D9D9D9",
    outline="")

sulfY_check = Checkbutton(canvas, onvalue=1, offvalue=0, variable=sulf_var, bg= '#D9D9D9')
sulfY_check.place(x = 535, y = 538)

canvas.create_text(
    562.0,
    542.0,
    anchor="nw",
    text="Sulfation of Y",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_rectangle(
    542.0,
    544.0,
    560.0,
    562.0,
    fill="#D9D9D9",
    outline="")
window.resizable(False, False)
window.mainloop()
