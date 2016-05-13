from whiningapp.whineapp import app
# from kelvinapp import settings - add when/if have settings file

# app.run(host=settings.web_host_address, port=settings.web_host_port, debug=True) - when have settings file
# When desiging can keep debug true.  If go live, turn it off or can be popped
app.run(debug=True)
# app.run()
