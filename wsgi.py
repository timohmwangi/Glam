def run_app():
    from app import create_app
    return create_app('development')


if __name__ == "__main__":
    from flaskwebgui import FlaskUI
    ui = FlaskUI(
        app=run_app(), 
        server="flask", 
        width=500, 
        height=500, 
        fullscreen=True 
    )
    ui.run()

