from flask import Blueprint, render_template, request, redirect, url_for, session, flash

viagens_bp = Blueprint("viagens", __name__, url_prefix="/viagens")