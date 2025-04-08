import tkinter as tk
import numpy as np 
import sys
from tkinter import filedialog


from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import TemperatureFit.TemperatureFitting as tfit
import TemperatureFit.SpeFile as spe

default_calubration_temperature = 2500

class LogoDisplay(tk.Frame):
    def __init__(self,container,x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)

        #Frame visual configuration
        self.configure(width=1260,height=40,background="White", highlightbackground="black", highlightthickness=1)

        #Frame position information
        self.place(x = x_position, y = y_position)

        #Set logo
        self.logotext = tk.Label(self, text="High T : Acton-PIXIS 400", font=('Helvetica', 20), background="White")
        self.logotext.place(x = 5, y = 0, width=1250, height=35)

class CalibrationFileSelection(tk.Frame):
    def __init__(self, container, x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)
        
        #Frame visual configuration
        self.configure(width=320,height=320,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)

        #Left Side Calibration
        
        load_left_file = tk.Button(self, text="Select Left Calibration File", command=lambda: self.calibration_file_open_dialog(1), font=('Helvetica', 10))
        load_left_file.place(x = 10, y=10, width = 300, height=25)

        self.left_file_location = tk.Text(self, bg = "light gray", font=('Helvetica', 10))#, relief=tk.FLAT)
        self.left_file_location.place(x = 10, y=45, width = 300, height=50) 

        self.set_left_temperature = tk.Text(self, background="light gray", font=('Helvetica', 10))
        self.set_left_temperature.place(x=210, y=100, width = 100, height=25)

        set_left_temperature_label = tk.Label(self, text="Left Calib. Temperature (K)",  borderwidth=2, relief="groove", background="white", font=('Helvetica', 10))
        set_left_temperature_label.place(x=10, y=100, width = 200, height=25)

        self.set_left_temperature.insert("end-1c", default_calubration_temperature)

        #Right Side Calibration
        
        load_right_file = tk.Button(self, text="Select Right Calibration File", command=lambda: self.calibration_file_open_dialog(2), font=('Helvetica', 10))
        load_right_file.place(x = 10, y=150, width = 300, height=25)

        self.right_file_location = tk.Text(self, bg = "light gray", font=('Helvetica', 10))#, relief=tk.FLAT)
        self.right_file_location.place(x = 10, y=185, width = 300, height=50) 

        self.set_right_temperature = tk.Text(self, background="light gray", font=('Helvetica', 10))
        self.set_right_temperature.place(x=210, y=240, width = 100, height=25)

        set_right_temperature_label = tk.Label(self, text="Right Calib. Temperature (K)",  borderwidth=2, relief="groove", background="white", font=('Helvetica', 10))
        set_right_temperature_label.place(x=10, y=240, width = 200, height=25)

        self.set_right_temperature.insert("end-1c", default_calubration_temperature)
    

    def calibration_file_open_dialog(self, file_location_number):
        #Differentiates between the light field spectra and the t-rax folder
        open_file_path = filedialog.askopenfilename()
        if file_location_number == 1:
            #print(open_file_name)
            self.left_file_location.config(state="normal")
            self.left_file_location.delete("1.0",tk.END)
            self.left_file_location.insert(tk.END, open_file_path)
            self.left_file_location.config(state="disabled")
        elif file_location_number == 2:
            self.right_file_location.config(state="normal")
            self.right_file_location.delete("1.0",tk.END)
            self.right_file_location.insert(tk.END, open_file_path)
            self.right_file_location.config(state="disabled")        
    
class TransmissionFilterSelection(tk.Frame):
    def __init__(self, container, x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)

        #Frame visual configuration
        self.configure(width=930,height=250,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        #self.place(x = self.x_position, y = self.y_position)

        self.select_one_transmission_filter_logo = tk.Label(self, text = "Select One Transmission Filter", font=('Helvetica', 15), background="White")
        self.select_one_transmission_filter_logo.place(x=5,y=5, width=920, height=30)

        self.select_one_transmission_filter_logo = tk.Label(self, text = "Select Iris Status", font=('Helvetica', 15), background="White")
        self.select_one_transmission_filter_logo.place(x=5,y=135, width=920, height=30)
        
        # Filter Determination Raio Buttons for the Left Side
        
        self.filter_variable_left = tk.IntVar()
        self.iris_variable_left = tk.IntVar()

        self.left_no_filter_selection = tk.Radiobutton(self,text="NO FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 1000, selectcolor="Light Blue", background="Light Blue")
        self.left_no_filter_selection.place(x=30, y = 50, width=90, height=30)
        self.left_no_filter_selection.select()

        self.left_700_filter_selection = tk.Radiobutton(self,text="70% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 700, selectcolor="Light Blue", background="Light Blue")
        self.left_700_filter_selection.place(x=130, y = 50, width=90, height=30)

        self.left_500_filter_selection = tk.Radiobutton(self,text="50% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 500, selectcolor="Light Blue", background="Light Blue")
        self.left_500_filter_selection.place(x=230, y = 50, width=90, height=30)

        self.left_350_filter_selection = tk.Radiobutton(self,text="35% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 350, selectcolor="Light Blue", background="Light Blue")
        self.left_350_filter_selection.place(x=330, y = 50, width=90, height=30)
        
        self.left_100_filter_selection = tk.Radiobutton(self,text="10% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 100, selectcolor="Light Blue", background="Light Blue")
        self.left_100_filter_selection.place(x=30, y = 90, width=90, height=30)

        self.left_070_filter_selection = tk.Radiobutton(self,text="7% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 70, selectcolor="Light Blue", background="Light Blue")
        self.left_070_filter_selection.place(x=130, y = 90, width=90, height=30)

        self.left_050_filter_selection = tk.Radiobutton(self,text="5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 50, selectcolor="Light Blue", background="Light Blue")
        self.left_050_filter_selection.place(x=230, y = 90, width=90, height=30)

        self.left_035_filter_selection = tk.Radiobutton(self,text="3.5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 35, selectcolor="Light Blue", background="Light Blue")
        self.left_035_filter_selection.place(x=330, y = 90, width=90, height=30)

        self.left_iris_selection = tk.Radiobutton(self, text = "Iris Out", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_left, value = 1, selectcolor="Light Blue", background="Light Blue")
        self.left_iris_selection.place(x = 130, y = 160, width=90, height=50)
        
        self.left_iris_selection = tk.Radiobutton(self, text = "Iris In", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_left, value = 0, selectcolor="Light Blue", background="Light Blue")
        self.left_iris_selection.place(x = 230, y = 160, width=90, height=50)

        # Filter Determination Raio Buttons for the Right Side
        
        self.filter_variable_right = tk.IntVar()
        self.iris_variable_right = tk.IntVar()

        self.right_no_filter_selection = tk.Radiobutton(self,text="NO FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 1000, selectcolor="Pink", background="Pink")
        self.right_no_filter_selection.place(x=930-90-330, y = 50, width=90, height=30)
        self.right_no_filter_selection.select()

        self.right_700_filter_selection = tk.Radiobutton(self,text="70% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 700, selectcolor="Pink", background="Pink")
        self.right_700_filter_selection.place(x=930-90-230, y = 50, width=90, height=30)

        self.right_500_filter_selection = tk.Radiobutton(self,text="50% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 500, selectcolor="Pink", background="Pink")
        self.right_500_filter_selection.place(x=930-90-130, y = 50, width=90, height=30)

        self.right_350_filter_selection = tk.Radiobutton(self,text="35% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 350, selectcolor="Pink", background="Pink")
        self.right_350_filter_selection.place(x=930-90-30, y = 50, width=90, height=30)
        
        self.right_100_filter_selection = tk.Radiobutton(self,text="10% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 100, selectcolor="Pink", background="Pink")
        self.right_100_filter_selection.place(x=930-90-330, y = 90, width=90, height=30)

        self.right_070_filter_selection = tk.Radiobutton(self,text="7% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 70, selectcolor="Pink", background="Pink")
        self.right_070_filter_selection.place(x=930-90-230, y = 90, width=90, height=30)

        self.right_050_filter_selection = tk.Radiobutton(self,text="5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 50, selectcolor="Pink", background="Pink")
        self.right_050_filter_selection.place(x=930-90-130, y = 90, width=90, height=30)

        self.right_035_filter_selection = tk.Radiobutton(self,text="3.5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 35, selectcolor="Pink", background="Pink")
        self.right_035_filter_selection.place(x=930-90-30, y = 90, width=90, height=30)

        self.right_iris_selection = tk.Radiobutton(self, text = "Iris Out", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_right, value = 1, selectcolor="Pink", background="Pink")
        self.right_iris_selection.place(x = 930-90-230, y = 160, width=90, height=50)
        
        self.right_iris_selection = tk.Radiobutton(self, text = "Iris In", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_right, value = 0, selectcolor="Pink", background="Pink")
        self.right_iris_selection.place(x = 930-90-130, y = 160, width=90, height=50)

class PlotGraphs(tk.Frame):
    def __init__(self, container, x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)

        #Frame visual configuration
        self.configure(width=930,height=640,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)

        self.wavelengths = np.arange(1, 101)
        self.left_fit = np.arange(1, 101)
        self.right_fit = np.arange(1, 101)
        self.left_raw = np.arange(1, 101)
        self.right_raw = np.arange(1, 101)

        self.fig, self.axis = plt.subplots(2, 2)
        plt.tight_layout()
        self.axis[0, 0].plot(self.wavelengths, self.left_fit)
        self.axis[0, 0].set_title('LEFT FIT')

        self.axis[0, 1].plot(self.wavelengths, self.right_fit, 'tab:orange')
        self.axis[0, 1].set_title('RIGHT FIT')
        self.axis[1, 0].plot(self.wavelengths, self.left_raw, 'tab:green')
        self.axis[1, 0].set_title('LEFT RAW')
        self.axis[1, 1].plot(self.wavelengths, self.right_raw, 'tab:red')
        self.axis[1, 1].set_title('RIGHT RAW')        
        
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().place(x = 0, y = 0, width=928,height=638)

        self.left_temperature_label = tk.Label(self, text="TEST", font=('Helvetica', 15), background="White")
        self.left_temperature_label.place(x=10, y= 10, width = 200, height = 50)

        self.left_calibration_temperature = 2255
        self.right_calibration_temperature = 2255
        #self.left_calibration_file = spe.SpeFile(r"T_Calib_20250314\15xMag\15xL\L_2255K_15x_wI.spe")
        #self.right_calibration_file = spe.SpeFile(r"T_Calib_20250314\15xMag\15xR\R_2255K_15x_wI.spe")
        #self.data_file = spe.SpeFile(r"T_Calib_20250314\15xMag\15xR\R_2255K_15x_wI.sp")
        #self.update_graphs()

    def update_graphs(self):
        A = self.left_calibration_file
        B = self.data_file
        C = self.right_calibration_file


        ccd_information = A.img
        ccd_data_size = np.shape(A.img)

        ccd_information2 = B.img
        ccd_data_size2 = np.shape(B.img)

        ccd_information3 = C.img
        ccd_data_size3 = np.shape(C.img)


        #Setting an ROI for testing purposes 
        self.left_roi_xo = 50
        self.left_roi_xf = 1004
        self.left_roi_yo = 13
        self.left_roi_yf = 27

        self.right_roi_xo = 50
        self.right_roi_xf = 1004
        self.right_roi_yo = 41
        self.right_roi_yf = 55

        
        #Setting an ROI for testing purposes 
        self.left_roi_xo = 1
        self.left_roi_xf = 1339
        self.left_roi_yo = 0
        self.left_roi_yf = 34

        self.right_roi_xo = 1
        self.right_roi_xf = 1339
        self.right_roi_yo = 35
        self.right_roi_yf = 69
        
        #print(A.x_calibration)
        #print(A.roi_width)
        #print(A.roi_y)
        #print(A.roi_height)
        
        
        #Left Spectrum
        left_x_axis_wavelengths = A.x_calibration[self.left_roi_xo:self.left_roi_xf]        
        left_y_axis_ccd_selected_region = ccd_information[self.left_roi_yo:self.left_roi_yf, self.left_roi_xo:self.left_roi_xf]
        left_calibration_summed_ccd_selected_region = np.sum(left_y_axis_ccd_selected_region,axis=0)
        
        left_x_axis_wavelengths = B.x_calibration[self.left_roi_xo:self.left_roi_xf]
        left_y_axis_ccd_selected_region = ccd_information2[self.left_roi_yo:self.left_roi_yf, self.left_roi_xo:self.left_roi_xf]
        left_summed_ccd_selected_region = np.sum(left_y_axis_ccd_selected_region,axis=0)

        #Right Spectrum
        right_x_axis_wavelengths = C.x_calibration[self.right_roi_xo:self.right_roi_xf]        
        right_y_axis_ccd_selected_region = ccd_information3[self.right_roi_yo:self.right_roi_yf, self.right_roi_xo:self.right_roi_xf]
        right_calibration_summed_ccd_selected_region = np.sum(right_y_axis_ccd_selected_region,axis=0)
        
        right_x_axis_wavelengths = B.x_calibration[self.right_roi_xo:self.right_roi_xf]
        right_y_axis_ccd_selected_region = ccd_information2[self.right_roi_yo:self.right_roi_yf, self.right_roi_xo:self.right_roi_xf]
        right_summed_ccd_selected_region = np.sum(right_y_axis_ccd_selected_region,axis=0)

        # Setting threshold to maximum size
        np.set_printoptions(threshold=sys.maxsize)
        #print(right_x_axis_wavelengths, right_calibration_summed_ccd_selected_region, right_summed_ccd_selected_region)    
        
        #Call the Temperature fitting class to get data for fit
        Estimated_Temperature_Left = tfit.Temperature_Measurement(1500, 0.5, self.left_calibration_temperature, left_x_axis_wavelengths, left_calibration_summed_ccd_selected_region, left_summed_ccd_selected_region)
        Estimated_Temperature_Right = tfit.Temperature_Measurement(1500, 0.5, self.right_calibration_temperature, right_x_axis_wavelengths, right_calibration_summed_ccd_selected_region, right_summed_ccd_selected_region)           

        self.left_wavelengths = left_x_axis_wavelengths
        self.left_fit = Estimated_Temperature_Left.gray_body_spectrum
        self.left_corrected = Estimated_Temperature_Left.unknown_graybody_spectrum
        self.left_raw = left_summed_ccd_selected_region

        self.right_wavelengths = right_x_axis_wavelengths
        self.right_fit = Estimated_Temperature_Right.gray_body_spectrum
        self.right_corrected = Estimated_Temperature_Right.unknown_graybody_spectrum
        self.right_raw = right_summed_ccd_selected_region

        
        #self.fig, self.axis = plt.subplots(2, 2)
        #plt.tight_layout()

        self.axis[0, 0].clear()
        self.axis[0, 0].plot(self.left_wavelengths, self.left_corrected, self.left_wavelengths, self.left_fit)
        self.axis[0, 0].set_title('LEFT FIT')

        self.axis[0, 1].clear()
        self.axis[0, 1].plot(self.right_wavelengths, self.right_corrected, self.right_wavelengths, self.right_fit)
        self.axis[0, 1].set_title('RIGHT FIT')

        self.axis[1, 0].clear()
        self.axis[1, 0].plot(self.left_wavelengths, self.left_raw)
        self.axis[1, 0].set_title('LEFT RAW')

        self.axis[1, 1].clear()
        self.axis[1, 1].plot(self.right_wavelengths, self.right_raw)
        self.axis[1, 1].set_title('RIGHT RAW')
 
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().place(x = 0, y = 0, width=928, height=638)
        
        left_temperature_string = "T= " + str(round(Estimated_Temperature_Left.fit_T)) + " +/- " + str(round(Estimated_Temperature_Left.sigT)) + " K"
        right_temperature_string = "T= " + str(round(Estimated_Temperature_Right.fit_T)) + " +/- " + str(round(Estimated_Temperature_Right.sigT)) + " K"

        # Place the labels containing the temepratures of the fit
        self.left_temperature_label = tk.Label(self, text=left_temperature_string, font=('Helvetica', 15), background="White", anchor="w")# highlightbackground="black", highlightthickness=1)
        self.left_temperature_label.place(x=77, y= 30, width = 200, height = 30)

        self.left_temperature_label = tk.Label(self, text=right_temperature_string, font=('Helvetica', 15), background="White", anchor="w")# highlightbackground="black", highlightthickness=1)
        self.left_temperature_label.place(x=530, y= 30, width = 200, height = 30)
      
class DataFileHandling(tk.Frame):
    def __init__(self, container, temperature_plots, calibration_files, x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)
        
        #Frame visual configuration
        self.configure(width=320,height=320,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.place(x = x_position, y = y_position)
        self.plots = temperature_plots
        self.calibration_files = calibration_files

        #Frame buttons and labels
        self.select_lightfield_spectra = tk.Button(self, text="Select Single .spe for T-fit", font=('Helvetica', 10), command=lambda: self.data_file_open_dialog(1))
        self.select_lightfield_spectra.place(x = 10, y = 10, width=300, height = 30)
        self.selected_lightfield_spectra = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.selected_lightfield_spectra.place(x = 10, y = 50, width=300, height = 50)

        self.select_folder_to_save_tfit = tk.Button(self, text="Select Folder for T-fit", font=('Helvetica', 10), command=lambda: self.data_file_open_dialog(2))
        self.select_folder_to_save_tfit.place(x = 10, y = 110, width=300, height = 30)
        self.selected_folder_to_save_tfit = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.selected_folder_to_save_tfit.place(x = 10, y = 150, width=300, height = 50)

        self.enter_output_filename = tk.Label(self, text="Enter output filename", font=('Helvetica', 10))
        self.enter_output_filename.place(x = 10, y = 210, width=300, height = 30)
        self.entered_output_filename = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.entered_output_filename.place(x = 10, y = 240, width=300, height = 30)

    def data_file_open_dialog(self, file_location_number):
        #Differentiates between the light field spectra and the t-rax folder
        if file_location_number == 1:
            self.open_file_path = filedialog.askopenfilename(filetypes=[("Lightfield spectrum", "*.spe"), ("All files", "*.*")])
            #print(open_file_name)
            self.selected_lightfield_spectra.delete("1.0",tk.END)
            self.selected_lightfield_spectra.insert(tk.END, self.open_file_path)

            #print(r'{}'.format(self.open_file_path))
            #self.plots.update_test()

            #Update the calibration files and temperatures
            left_calibration_file_location = r"{}".format(self.calibration_files.left_file_location.get("1.0",tk.END))            
            left_calibration_file_location = left_calibration_file_location.replace("\n", "")

            right_calibration_file_location = r"{}".format(self.calibration_files.right_file_location.get("1.0",tk.END))
            right_calibration_file_location = right_calibration_file_location.replace("\n", "")

            #Update the calibration temperature values
            left_calibration_temperature = float(self.calibration_files.set_left_temperature.get("1.0",tk.END))
            right_calibration_temperature = float(self.calibration_files.set_left_temperature.get("1.0",tk.END))

            #Update the values in the plots class
            self.plots.left_calibration_temperature = left_calibration_temperature
            self.plots.right_calibration_temperature = right_calibration_temperature
            self.plots.left_calibration_file = spe.SpeFile(left_calibration_file_location)
            self.plots.right_calibration_file = spe.SpeFile(right_calibration_file_location)
            self.plots.data_file = spe.SpeFile(r'{}'.format(self.open_file_path))
            self.plots.update_graphs()
            
        elif file_location_number == 2:
            self.open_folder_path = filedialog.askdirectory()
            #print(open_file_name)
            self.selected_folder_to_save_tfit.delete("1.0",tk.END)
            self.selected_folder_to_save_tfit.insert(tk.END, self.open_folder_path)        

class InitiateActonTfit(tk.Frame):
    #def __init__(self, x_position, y_position):
    #    tk.Frame.__init__(self)
    def __init__(self, container, x_position, y_position):
        #tk.Frame.__init__(self, container)
        super().__init__(container)

        #Frame visual configuration
        self.configure(width=1280,height=1000)
        
        #Frame position information
        self.place(x = x_position, y = y_position)

        self.Logo = LogoDisplay(self, 10,10)
        # CalibrationFile = CalibrationFileSelection(10, 360)
        self.TransmissionFilter = TransmissionFilterSelection (self, 340, 60)
        self.TransmissionFilter.place(x = 340, y = 60)

        self.Tempreature_graphs = PlotGraphs(self, 340, 320)
        self.CalibrationFileSelect = CalibrationFileSelection(self, 10, 90)
        self.DataFileSelect = DataFileHandling(self, self.Tempreature_graphs, self.CalibrationFileSelect, 10, 90)
        
        self.DataFileSelect_placedata = self.DataFileSelect.place_info()
        self.CalibrationFileSelect_placedata = self.CalibrationFileSelect.place_info()

        self.show_data_selection_window = tk.Button(self, text="Temperature Fit", command=lambda: self.select_file_handling(2))
        self.show_data_selection_window.place(x = 170, y = 60, width = 160, height = 25)
        self.show_data_selection_window.config(state="disable")

        #Buttons for showing the correct file handling window
        self.show_calibration_selection_window = tk.Button(self, text="Calibration Selection", command=lambda: self.select_file_handling(1))
        self.show_calibration_selection_window.place(x = 10, y = 60, width = 160, height = 25)
        self.show_calibration_selection_window.config(state="active")

    def select_file_handling(self, input):
        x = 0
        if input == 1:
            self.DataFileSelect.place_forget()
            self.CalibrationFileSelect.place(self.CalibrationFileSelect_placedata)
            self.show_data_selection_window.config(state="active")
            self.show_calibration_selection_window.config(state="disabled")
        elif input == 2:
            self.CalibrationFileSelect.place_forget()
            self.DataFileSelect.place(self.DataFileSelect_placedata)
            self.show_calibration_selection_window.config(state="active")
            self.show_data_selection_window.config(state="disabled")


if __name__ == "__main__":

    mainwindow = tk.Tk()
    mainwindow.geometry('1280x1000')
    mainwindow.title("High T: Acton-PIXIS 400")

    A = InitiateActonTfit(0,600)

    mainwindow.mainloop()


    