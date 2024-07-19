import scrapy
import urllib.parse

class TeamsSpider(scrapy.Spider):
    name = "teams"
    allowed_domains = ["sports.ru"]
    start_urls = ["https://sports.ru/hockey/tournament/nhl/table/"]

    def parse(self, response):
        clubs = response.xpath("//table[@class='stat-table']/tbody/tr/td[2]/div/a")

        for club in clubs:
            name = club.xpath(".//text()").get().strip()
            link = club.xpath(".//@href").get()+'/stat/'
            #link = response.urljoin('/stat/')

            #absolute_url = response.urljoin(link)

            yield response.follow(url=link, callback=self.parse_team, meta={'team_name' : name})
    
    def parse_team(self, response):
        name = response.request.meta['team_name']
        rows = response.xpath("//table[@class='stat-table js-active']/tbody/tr")

        for row in rows:
            No = row.xpath(".//td[1]/text()").get().strip()
            Player_Name = row.xpath(".//td[2]/a/text()").get().strip()
            Games_Played = row.xpath(".//td[4]/text()").get().strip()
            Goals = row.xpath(".//td[5]/text()").get().strip()
            Assists = row.xpath(".//td[6]/text()").get().strip()
            Points = row.xpath(".//td[7]/text()").get().strip().strip()
            
        
            yield {
                'Team': name if name else '',
                'No' : No if No else '',
                'Player_Name' : Player_Name if Player_Name else '',
                'Games_Played' : int(Games_Played) if Games_Played else 0,
                'Goals': int(Goals) if Goals else 0,
                'Assists': int(Assists) if Assists else 0,
                'Points': int(Points) if Points else 0                    
            }