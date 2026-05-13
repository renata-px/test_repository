from pathlib import Path
from shiny import ui, render, reactive, App
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from calculations import *
from opt_func import simple_ga_optimize_pyr

www_dir = Path(__file__).parent / "www"

# Refactored Shiny App - calculations moved to calculations.py

app_ui = ui.page_fluid(
    ui.h1("CEET Refactored App - Calculations Separated")
)

def server(input, output, session):
    @reactive.Calc
    def current_temp():
        return normal_temp_c(input.x1(), input.x2(), input.x3())
    
    @output
    @render.text
    def temp_display():
        return f"Normalized temp: {current_temp():.1f} °C"

app = App(app_ui, server, static_assets=www_dir)
print('✅ Refactored app.py loaded successfully')