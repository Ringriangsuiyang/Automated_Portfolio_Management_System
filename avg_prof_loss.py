import pandas as pd
import yfinance as yf

symbol_list=['AARTIIND.NS', 'ABB.NS', 'ABBOTINDIA.NS', 'ABCAPITAL.NS', 'ABFRL.NS', 'ACC.NS', 'ADANIENT.NS', 'ADANIPORTS.NS', 'ALKEM.NS', 'AMARAJABAT.NS', 'AMBUJACEM.NS', 'APOLLOHOSP.NS', 'APOLLOTYRE.NS', 'ASHOKLEY.NS', 'ASIANPAINT.NS', 'ASTRAL.NS', 'ATUL.NS', 'AUBANK.NS', 'AUROPHARMA.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BALKRISIND.NS', 'BALRAMCHIN.NS', 'BANDHANBNK.NS', 'BANKBARODA.NS', 'BATAINDIA.NS', 'BEL.NS', 'BERGEPAINT.NS', 'BHARATFORG.NS', 'BHARTIARTL.NS', 'BHEL.NS', 'BIOCON.NS', 'BOSCHLTD.NS', 'BPCL.NS', 'BRITANNIA.NS', 'BSOFT.NS', 'CANBK.NS', 'CANFINHOME.NS', 'CHAMBLFERT.NS', 'CHOLAFIN.NS', 'CIPLA.NS', 'COALINDIA.NS', 'COFORGE.NS', 'COLPAL.NS', 'CONCOR.NS', 'COROMANDEL.NS', 'CROMPTON.NS', 'CUB.NS', 'CUMMINSIND.NS', 'DABUR.NS', 'DALBHARAT.NS', 'DEEPAKNTR.NS', 'DELTACORP.NS', 'DIVISLAB.NS', 'DIXON.NS', 'DLF.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'ESCORTS.NS', 'EXIDEIND.NS', 'FEDERALBNK.NS', 'FSL.NS', 'GAIL.NS', 'GLENMARK.NS', 'GMRINFRA.NS', 'GNFC.NS', 'GODREJCP.NS', 'GODREJPROP.NS', 'GRANULES.NS', 'GRASIM.NS', 'GSPL.NS', 'GUJGASLTD.NS', 'HAL.NS', 'HAVELLS.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCAMC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDCOPPER.NS', 'HINDPETRO.NS', 'HINDUNILVR.NS', 'HONAUT.NS', 'IBULHSGFIN.NS', 'ICICIBANK.NS', 'ICICIGI.NS', 'ICICIPRULI.NS', 'IDEA.NS', 'IDFC.NS', 'IDFCFIRSTB.NS', 'IEX.NS', 'IGL.NS', 'INDHOTEL.NS', 'INDIACEM.NS', 'INDIAMART.NS', 'INDIGO.NS', 'INDUSINDBK.NS', 'INDUSTOWER.NS', 'INFY.NS', 'INTELLECT.NS', 'IOC.NS', 'IPCALAB.NS', 'IRCTC.NS', 'ITC.NS', 'JINDALSTEL.NS', 'JKCEMENT.NS', 'JSWSTEEL.NS', 'JUBLFOOD.NS', 'KOTAKBANK.NS', 'L&TFH.NS', 'LALPATHLAB.NS', 'LAURUSLABS.NS', 'LICHSGFIN.NS', 'LT.NS', 'LTI.NS', 'LTTS.NS', 'LUPIN.NS', 'M&M.NS', 'M&MFIN.NS', 'MANAPPURAM.NS', 'MARICO.NS', 'MARUTI.NS', 'MCDOWELL-N.NS', 'MCX.NS', 'METROPOLIS.NS', 'MFSL.NS', 'MGL.NS', 'MINDTREE.NS', 'MOTHERSON.NS', 'MPHASIS.NS', 'MRF.NS', 'MUTHOOTFIN.NS', 'NATIONALUM.NS', 'NAUKRI.NS', 'NAVINFLUOR.NS', 'NESTLEIND.NS', 'NMDC.NS', 'NTPC.NS', 'OBEROIRLTY.NS', 'OFSS.NS', 'ONGC.NS', 'PAGEIND.NS', 'PEL.NS', 'PERSISTENT.NS', 'PETRONET.NS', 'PFC.NS', 'PIDILITIND.NS', 'PIIND.NS', 'PNB.NS', 'POLYCAB.NS', 'POWERGRID.NS', 'PVR.NS', 'RAIN.NS', 'RAMCOCEM.NS', 'RBLBANK.NS', 'RECLTD.NS', 'RELIANCE.NS', 'SAIL.NS', 'SBICARD.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SIEMENS.NS', 'SRF.NS', 'SRTRANSFIN.NS', 'SUNPHARMA.NS', 'SUNTV.NS', 'SYNGENE.NS', 'TATACHEM.NS', 'TATACOMM.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATAPOWER.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'TORNTPHARM.NS', 'TORNTPOWER.NS', 'TRENT.NS', 'TVSMOTOR.NS', 'UBL.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'VEDL.NS', 'VOLTAS.NS', 'WHIRLPOOL.NS', 'WIPRO.NS', 'ZEEL.NS', 'ZYDUSLIFE.NS']
stock_names = ["Aarti Industries Limited","ABB India Limited","Abbott India Limited","Aditya Birla Capital Limited","Aditya Birla Fashion and Retail Limited","ACC Limited","Adani Enterprises Limited","Adani Ports and Special Economic Zone Limited","Alkem Laboratories Limited","Amara Raja Batteries Limited","Ambuja Cements Limited","Apollo Hospitals Enterprise Limited","Apollo Tyres Limited","Ashok Leyland Limited","Asian Paints Limited","Astral Limited","Atul Ltd","AU Small Finance Bank Limited","Aurobindo Pharma Limited","Axis Bank Limited","Bajaj Auto Limited","Bajaj Finserv Ltd.","Bajaj Finance Limited","Balkrishna Industries Limited","Balrampur Chini Mills Limited","Bandhan Bank Limited","Bank of Baroda","Bata India Limited","Bharat Electronics Limited","Berger Paints India Limited","Bharat Forge Limited","Bharti Airtel Limited","Bharat Heavy Electricals Limited","Biocon Limited","Bosch Limited","Bharat Petroleum Corporation Limited","Britannia Industries Limited","Birlasoft Limited","Canara Bank","Can Fin Homes Limited","Chambal Fertilisers and Chemicals Limited","Cholamandalam Investment and Finance Company Limited","Cipla Limited","Coal India Limited","Coforge Limited","Colgate-Palmolive (India) Limited","Container Corporation of India Limited","Coromandel International Limited","Crompton Greaves Consumer Electricals Limited","City Union Bank Limited","Cummins India Limited","Dabur India Limited","Dalmia Bharat Limited","Deepak Nitrite Limited","Delta Corp Limited","Divi's Laboratories Limited","Dixon Technologies (India) Limited","DLF Limited","Dr. Reddy's Laboratories Limited","Eicher Motors Limited","Escorts Kubota Limited","Exide Industries Limited","The Federal Bank Limited","Firstsource Solutions Limited","GAIL (India) Limited","Glenmark Pharmaceuticals Limited","GMR Airports Infrastructure Limited","Gujarat Narmada Valley Fertilizers & Chemicals Limited","Godrej Consumer Products Limited","Godrej Properties Limited","Granules India Limited","Grasim Industries Limited","Gujarat State Petronet Limited","Gujarat Gas Limited","Hindustan Aeronautics Limited","Havells India Limited","HCL Technologies Limited","Housing Development Finance Corporation Limited","HDFC Asset Management Company Limited","HDFC Bank Limited","HDFC Life Insurance Company Limited","Hero MotoCorp Limited","Hindalco Industries Limited","Hindustan Copper Limited","Hindustan Petroleum Corporation Limited","Hindustan Unilever Limited","Honeywell Automation India Limited","Indiabulls Housing Finance Limited","ICICI Bank Limited","ICICI Lombard General Insurance Company Limited","ICICI Prudential Life Insurance Company Limited","Vodafone Idea Limited","IDFC Limited","IDFC First Bank Limited","Indian Energy Exchange Limited","Indraprastha Gas Limited","The Indian Hotels Company Limited","The India Cements Limited","IndiaMART InterMESH Limited","InterGlobe Aviation Limited","IndusInd Bank Limited","Indus Towers Limited","Infosys Limited","Intellect Design Arena Limited","Indian Oil Corporation Limited","Ipca Laboratories Limited","Indian Railway Catering & Tourism Corporation Limited","ITC Limited","Jindal Steel & Power Limited","J.K. Cement Limited","JSW Steel Limited","Jubilant FoodWorks Limited","Kotak Mahindra Bank Limited","L&T Finance Holdings Limited","Dr. Lal PathLabs Limited","Laurus Labs Limited","LIC Housing Finance Limited","Larsen & Toubro Limited","Larsen & Toubro Infotech Limited","L&T Technology Services Limited","Lupin Limited","Mahindra & Mahindra Limited","Mahindra & Mahindra Financial Services Limited","Manappuram Finance Limited","Marico Limited","Maruti Suzuki India Limited","United Spirits Limited","Multi Commodity Exchange of India Limited","Metropolis Healthcare Limited","Max Financial Services Limited","Mahanagar Gas Limited","Mindtree Limited","Samvardhana Motherson International Limited","Mphasis Limited","MRF Limited","Muthoot Finance Limited","National Aluminium Company Limited","Info Edge (India) Limited","Navin Fluorine International Limited","Nestlé India Limited","NMDC Limited","NTPC Limited","Oberoi Realty Limited","Oracle Financial Services Software Limited","Oil and Natural Gas Corporation Limited","Page Industries Limited","Piramal Enterprises Limited","Persistent Systems Limited","Petronet LNG Limited","Power Finance Corporation Limited","Pidilite Industries Limited","PI Industries Limited","Punjab National Bank","Polycab India Limited","Power Grid Corporation of India Limited","PVR Limited","Rain Industries Limited","The Ramco Cements Limited","RBL Bank Limited","REC Limited","Reliance Industries Limited","Steel Authority of India Limited","SBI Cards and Payment Services Limited","SBI Life Insurance Company Limited","State Bank of India","Shree Cement Limited","Siemens Limited","SRF Limited","Shriram Transport Finance Company Limited","Sun Pharmaceutical Industries Limited","Sun TV Network Limited","Syngene International Limited","Tata Chemicals Limited","Tata Communications Limited","Tata Consumer Products Limited","Tata Motors Limited","The Tata Power Company Limited","Tata Steel Limited","Tata Consultancy Services Limited","Tech Mahindra Limited","Titan Company Limited","Torrent Pharmaceuticals Limited","Torrent Power Limited","Trent Limited","TVS Motor Company Limited","United Breweries Limited","UltraTech Cement Limited","UPL Limited","Vedanta Limited","Voltas Limited","Whirlpool of India Limited","Wipro Limited","Zee Entertainment Enterprises Limited","Zydus Lifesciences Limited"]

year = ['2017-01-01','2018-01-01', '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01']

total_trades = []
win_ratio = []
avg_loss = []
avg_profit = []
l_li = []
p_li = []

for j in range(1):
    profit_final = []
    for k in range(len(symbol_list)):
        symbol = symbol_list[k]
        try:  
            df = yf.download(symbol, start = year[j], end = year[j+5], interval = '1wk', rounding = True)

            df = df.dropna()
            df = df.reset_index()

            risk = 0.01
            vc = 1000000
            rpt = risk * vc

            #for buy then sell
            status = 0
            quantity = 0
            buy_profit = 0
            Entry = 0
            t1 = 0
            t2 = 0
            Fixed_Sl = 0
            Trailing_Sl = 0
            sl = 0
            t1_status = 0
            t2_status = 0
            date=""
            date_exit=""
            #for sell then buy
            sell_status = 0
            sell_quantity = 0
            sell_profit = 0
            sell_Entry = 0
            sell_t1 = 0
            sell_t2 = 0
            sell_Fixed_Sl = 0
            sell_Trailing_Sl = 0
            sell_sl = 0
            sell_t1_status = 0
            sell_t2_status = 0
            sell_date=""

            profit = 0
            loss =  0
            p = 0
            l = 0

            for i in range(2, len(df)):
                try:
            
                 #For Buy then Sell
                    if (status == 0):
                        Entry = max(df['High'][i-2], df['High'][i-1])
                        t1 = round(Entry * 1.03, 2)
                        t2 = round(Entry * 1.06, 2)
                        chigh = df['High'][i]
                        Fixed_Sl = round(Entry * 0.97, 2)
                        Trailing_Sl = min(df['Low'][i-2], df['Low'][i-1])
                        sl = max(Fixed_Sl, Trailing_Sl)
                        if (chigh > Entry):
                            status = 1
                            date = df['Date'][i]
                            quantity = 1
                            #print("Date",df['Date'][i])    
                            #print("Entry",Entry)  
                    if status == 1:
                        Fixed_Sl = round(Entry * 0.97, 2)
                        Trailing_Sl = min(df['Low'][i-2], df['Low'][i-1])
                        sl = max(Fixed_Sl, Trailing_Sl)
                        chigh = df['High'][i]
                        if chigh > t1 and t1_status == 0:
                            exited_quantity = 0.33
                            buy_profit += 3 * exited_quantity
                            quantity =  quantity - exited_quantity
                            t1_status = 1
                        if chigh > t2 and t2_status == 0:
                            exited_quantity = quantity * 0.5
                            buy_profit += 6 * exited_quantity
                            quantity =  quantity - exited_quantity
                            t2_status = 1
                        if df['Low'][i] < sl and df['Date'][i] != date:
                            date_exit = df['Date'][i]
                            buy_profit += round((sl - Entry)*100/Entry*quantity,2)
                            if buy_profit>=0:
                                profit = profit + buy_profit
                                p+=1
                            else:
                                loss = loss - buy_profit
                                l+=1
                            quantity = 0
                            status = 0
                            t1_status = 0
                            t2_status = 0
                            buy_profit = 0
                            
                            #print("Exit",sl)

                    #for Sell then Buy
                    if (sell_status == 0):
                        sell_Entry = min(df['Low'][i-2], df['Low'][i-1])
                        sell_t1 = round(sell_Entry * 0.97, 2)
                        sell_t2 = round(sell_Entry * 0.94, 2)
                        clow = df['Low'][i]
                        sell_Fixed_Sl = round(sell_Entry * 1.03, 2)
                        sell_Trailing_Sl = max(df['High'][i-2], df['High'][i-1])
                        sell_sl = min(sell_Fixed_Sl, sell_Trailing_Sl)
                        if (clow < sell_Entry):
                            sell_status = 1
                            sell_date = df['Date'][i]
                            sell_quantity = 1
                            date=df['Date'][i]    
                    if sell_status == 1:
                        sell_Fixed_Sl = round(sell_Entry * 1.03, 2)
                        sell_Trailing_Sl = max(df['High'][i-2], df['High'][i-1])
                        sell_sl = min(sell_Fixed_Sl, sell_Trailing_Sl)
                        clow = df['Low'][i]
                        if clow < sell_t1 and sell_t1_status == 0:
                            exited_sell_quantity = 0.33
                            sell_profit += 3 * exited_sell_quantity
                            sell_quantity =  sell_quantity - exited_sell_quantity
                            sell_t1_status = 1
                        if clow < sell_t2 and sell_t2_status == 0:
                            exited_sell_quantity = sell_quantity * 0.5
                            sell_profit += 6 * exited_sell_quantity
                            sell_quantity =  sell_quantity - exited_sell_quantity
                            sell_t2_status = 1
                        if df['High'][i] > sell_sl and df['Date'][i] != sell_date:
                            sell_profit += round((sell_Entry - sell_sl)/sell_Entry*100* sell_quantity,2)
                            date_exit = df['Date'][i]
                            if sell_profit>=0:
                                profit = profit + sell_profit
                                p+=1
                            else:
                                loss = loss - sell_profit
                                l+=1
                            sell_quantity = 0
                            sell_status = 0
                            sell_t1_status = 0
                            sell_t2_status = 0
                            sell_profit = 0
                except:
                    pass 
            tt = p+l
            wr = round(p/tt*100,2)
            avg_rw = round(profit/p,2)
            avg_rr = round(loss/l,2)

            total_trades.append(tt)
            win_ratio.append(wr)
            avg_loss.append(avg_rr)
            avg_profit.append(avg_rw)
            l_li.append(l)
            p_li.append(p)
        except:
            avg_profit.append(0)
            total_trades.append(0)
            win_ratio.append(0)
            avg_loss.append(0)
            avg_profit.append(0)
            pass

stock_dict = {'Stock Name': stock_names, "total_trades": total_trades, "win_ratio": win_ratio, "avg_profit": avg_profit, "avg_loss": avg_loss}
stock_df = pd.DataFrame(stock_dict)
stock_df.to_csv("statistic_percent_debugged.csv")
print(stock_df)
