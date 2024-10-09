import flet as ft
from PIL import Image
#from financial_app import dtmodel1
import numpy as np
import joblib

def main(page: ft.page):
        #load data
        #model = joblib.load("financial_decision_tree.pkl")
        #feature_names = [
        #"amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest",
        #"newbalanceDest", "nameOrig_frq", "nameDest_frq", "type_CASH_IN",
        #"type_CASH_OUT", "type_DEBIT", "type_PAYMENT", "type_TRANSFER"
        #]

        t = ft.Container(content=ft.Text(value= "WELCOME!", color= "#640D5F", size= 25),
                        alignment= ft.alignment.center,
                        padding=50,
                        
                        )
        page.padding = 0
        
        page.update()
        transaction = ft.TextField(width=250,height=140)
        old_balance = ft.TextField(width=250,height=140)
        textfield = ft.Container(ft.Column(controls=[transaction,
                                                old_balance,
                                                
                                ],
                                scroll=ft.ScrollMode.AUTO, 
                                ),
                                alignment= ft.alignment.center,
                                padding=10
                                )
        
        addBtn = ft.Container(ft.TextButton("SUBMIT",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius = 10),
                                                bgcolor={ft.MaterialState.HOVERED: ft.colors.CYAN_700,
                                                        ft.MaterialState.DEFAULT: ft.colors.CYAN_600},
                                                ),
                        ),
                        width= 95,
                        )
        #stack = ft.Stack(
        #        [
        #        ft.Container(
        #        bgcolor=ft.colors.TRANSPARENT,  # Set the container background to transparent
        #        content=ft.Image(  # Correctly use the content parameter
        #                src="https://cdn.pixabay.com/photo/2017/08/01/23/51/apple-2568755_1280.jpg",
        #                fit=ft.ImageFit.CONTAIN,
        #                        ),
        #                opacity=0.5,
        #                ),
        #        t,
        #        ]
        #)
        page.add(t,textfield,ft.Container(addBtn,
                                        alignment=ft.alignment.center))
ft.app(main)