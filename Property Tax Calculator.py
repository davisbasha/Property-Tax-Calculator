import tkinter

class PropertyTaxApp:
    def __init__(self):
        #Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title('Property Tax Viewer')

        #Build the widgets.
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        #Start the main loop.
        tkinter.mainloop()

    #Prompt label for user.
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(
            self.main_window, text='Select a Property Value:')
        self.prompt_label.pack(padx=5, pady=5)

    #Listbox to show property values.
    def __build_listbox(self):

        self.__values = [5000, 10000, 25000, 50000, 75000, 100000]


        self.value_listbox = tkinter.Listbox(
            self.main_window, height=0, width=0)
        self.value_listbox.pack(padx=5, pady=5)


        self.value_listbox.bind(
            '<<ListboxSelect>>', self.__display_tax_info)

        #Add property values to the Listbox.
        for val in self.__values:
            self.value_listbox.insert(tkinter.END, f"${val:,}")

    #Frame for showing assessment and tax.
    def __build_output_frame(self):
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)

        #Labels and StringVars
        self.__assessment_var = tkinter.StringVar()
        self.__tax_var = tkinter.StringVar()


        self.assess_label = tkinter.Label(
            self.output_frame, text='Assessment Value:')
        self.assess_label.pack(pady=(5, 0))
        self.assess_output = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=20, textvariable=self.__assessment_var)
        self.assess_output.pack(pady=(0, 5))

        #Property Tax Display
        self.tax_label = tkinter.Label(
            self.output_frame, text='Property Tax:')
        self.tax_label.pack()
        self.tax_output = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=20, textvariable=self.__tax_var)
        self.tax_output.pack(pady=(0, 5))

    #Quit button.
    def __build_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Quit',
            command=self.main_window.destroy)
        self.quit_button.pack(pady=5)

    #Function to calculate and display tax details.
    def __display_tax_info(self, event):
        #Get selection
        index = self.value_listbox.curselection()
        if index:
            value_str = self.value_listbox.get(index[0])
            actual_value = int(value_str.replace('$', '').replace(',', ''))

            assessment = actual_value * 0.60
            tax = (assessment / 100) * 0.75

            self.__assessment_var.set(f"${assessment:,.2f}")
            self.__tax_var.set(f"${tax:,.2f}")

#Run the program
if __name__ == '__main__':
    app = PropertyTaxApp()