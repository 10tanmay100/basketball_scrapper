from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging as lg

app=Flask(__name__,template_folder="templates")
@app.route("/",methods=['GET', 'POST'])
def home():
	return render_template("index.html")
@app.route("/details",methods=['POST'])
def details():
	lg.basicConfig(filename="logger.log", level=lg.DEBUG, format='%(asctime)s %(message)s')
	player=[]
	lg.info("Connecting with the server")
	if request.method=="POST":
		team_name=request.form["team"]

		if team_name=="MIA":
			lg.info("choosing team name MIA")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
				lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="PHI":
			lg.info("choosing team name PHI")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="MIL":
			lg.info("choosing team name MIL")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="BOS":
			lg.info("choosing team name BOS")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="CHI":
			lg.info("choosing team name CHI")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="TOR":
			lg.info("choosing team name TOR")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="CLE":
			lg.info("choosing team name CLE")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="BRK":
			lg.info("choosing team name BRK")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="CHO":
			lg.info("choosing team name CHO")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="ATL":
			lg.info("choosing team name ATL")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="NYK":
			lg.info("choosing team name NYK")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="WAS":
			lg.info("choosing team name WAS")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="IND":
			lg.info("choosing team name IND")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="DET":
			lg.info("choosing team name DET")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="ORL":
			lg.info("choosing team name ORL")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="PHO":
			lg.info("choosing team name PHO")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="MEM":
			lg.info("choosing team name MEM")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="GSW":
			lg.info("choosing team name GSW")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="DAL":
			lg.info("choosing team name DAL")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="UTA":
			lg.info("choosing team name UTA")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="DEN":
			lg.info("choosing team name DEN")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="MIN":
			lg.info("choosing team name MIN")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="LAC":
			lg.info("choosing team name LAC")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="NOP":
			lg.info("choosing team name NOP")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="LAL":
			lg.info("choosing team name LAL")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="SAS":
			lg.info("choosing team name SAS")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="POR":
			lg.info("choosing team name POR")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="SAC":
			lg.info("choosing team name SAC")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="OKC":
			lg.info("choosing team name OKC")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		elif team_name=="HOU":
			lg.info("choosing team name HOU")
			url = f"https://www.basketball-reference.com/teams/{team_name}/2022.html"
			uClient = uReq(url)
			lg.debug("Requesting the link")
			basket_url = uClient.read()
			uClient.close()
			basket_html = bs(basket_url, "html.parser")
			lg.info("parsing html")
			val = basket_html.findAll("div", {"id": "content"})[0]
			t1 = val.findAll("div", {"class": "table_wrapper"})[0]
			first_table = t1.findAll("div", {"class": "table_container"})[0]
			table = first_table.findAll("table", {"class": "sortable"})[0]
			elements = ["Player", "Position", "Height", "Weight", "Bday", "Country", "Experience", "College"]
			dict1={}
			for i in range(1, len(table.findAll("tr"))):
				dict1 = {}
				No = table.findAll("tr")[i].th.text
				number=No
				dict1["No"]=number
				for j in range(8):
					dict1[elements[j]] = table.findAll("tr")[i].findAll("td")[j].text
				player.append(dict1)
			lg.info("Rendering data on html")
			return render_template('result.html', plyrs=player[0:(len(player)-1)])
		else:
			lg.error("Not able to connect")
			return "no"
app.run()










