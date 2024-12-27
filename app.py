from flask import Flask, request, jsonify
import pyodbc

app = Flask(_name_)

def scrap_data(URLS, County):
    from scraper.scraper import Scraper
    scraper = Scraper(URLS, County)
    result = scraper.scrape_site(County, URLS.split(',')[0], URLS.split(',')[0])
    return True

def get_connection():
    return pyodbc.connect('DRIVER={SQL Server};SERVER=devdb3;DATABASE=UnifiedSearchPortal;Trusted_Connection=yes')


def get_project(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Projects WHERE ID = ? AND SourceId = 1', id)
    return cursor.fetchone()


@app.route('/scrapping-requests/', methods=['POST'])
def scrapping_requests():
    data = request.get_json()

    if 'user_id' not in data or 'project_id' not in data:
        return jsonify({'error': 'Invalid data'})

    user_id = data['user_id']
    project_id = data['project_id']
    project = get_project(project_id)
    if not project:
        return 'Project not found'

    scrap_data(project[4], project[3])
    return jsonify({})


if _name_ == '_main_':
    app.run(debug=True)
