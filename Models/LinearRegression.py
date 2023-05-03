{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "809bb8b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0b4c05e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('data/stock_data/Reliance.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8974439a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Time</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2023-02-13 09:15:00</td>\n",
       "      <td>2340.20</td>\n",
       "      <td>2341.45</td>\n",
       "      <td>2337.05</td>\n",
       "      <td>2339.80</td>\n",
       "      <td>40926</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2023-02-13 09:16:00</td>\n",
       "      <td>2339.40</td>\n",
       "      <td>2340.80</td>\n",
       "      <td>2336.95</td>\n",
       "      <td>2340.25</td>\n",
       "      <td>20289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>2023-02-13 09:17:00</td>\n",
       "      <td>2340.80</td>\n",
       "      <td>2346.20</td>\n",
       "      <td>2340.75</td>\n",
       "      <td>2345.90</td>\n",
       "      <td>23981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>2023-02-13 09:18:00</td>\n",
       "      <td>2347.00</td>\n",
       "      <td>2350.00</td>\n",
       "      <td>2344.70</td>\n",
       "      <td>2345.35</td>\n",
       "      <td>31951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>2023-02-13 09:19:00</td>\n",
       "      <td>2345.00</td>\n",
       "      <td>2346.60</td>\n",
       "      <td>2344.00</td>\n",
       "      <td>2344.75</td>\n",
       "      <td>13916</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8245</th>\n",
       "      <td>8245</td>\n",
       "      <td>2023-03-15 15:25:00</td>\n",
       "      <td>2234.65</td>\n",
       "      <td>2234.80</td>\n",
       "      <td>2233.85</td>\n",
       "      <td>2234.35</td>\n",
       "      <td>39387</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8246</th>\n",
       "      <td>8246</td>\n",
       "      <td>2023-03-15 15:26:00</td>\n",
       "      <td>2234.35</td>\n",
       "      <td>2234.90</td>\n",
       "      <td>2234.00</td>\n",
       "      <td>2234.60</td>\n",
       "      <td>48522</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8247</th>\n",
       "      <td>8247</td>\n",
       "      <td>2023-03-15 15:27:00</td>\n",
       "      <td>2234.65</td>\n",
       "      <td>2235.25</td>\n",
       "      <td>2234.15</td>\n",
       "      <td>2235.15</td>\n",
       "      <td>50130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8248</th>\n",
       "      <td>8248</td>\n",
       "      <td>2023-03-15 15:28:00</td>\n",
       "      <td>2235.00</td>\n",
       "      <td>2238.20</td>\n",
       "      <td>2235.00</td>\n",
       "      <td>2236.10</td>\n",
       "      <td>71039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8249</th>\n",
       "      <td>8249</td>\n",
       "      <td>2023-03-15 15:29:00</td>\n",
       "      <td>2236.00</td>\n",
       "      <td>2237.45</td>\n",
       "      <td>2235.00</td>\n",
       "      <td>2237.45</td>\n",
       "      <td>45288</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8250 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Unnamed: 0                 Time     Open     High      Low    Close  \\\n",
       "0              0  2023-02-13 09:15:00  2340.20  2341.45  2337.05  2339.80   \n",
       "1              1  2023-02-13 09:16:00  2339.40  2340.80  2336.95  2340.25   \n",
       "2              2  2023-02-13 09:17:00  2340.80  2346.20  2340.75  2345.90   \n",
       "3              3  2023-02-13 09:18:00  2347.00  2350.00  2344.70  2345.35   \n",
       "4              4  2023-02-13 09:19:00  2345.00  2346.60  2344.00  2344.75   \n",
       "...          ...                  ...      ...      ...      ...      ...   \n",
       "8245        8245  2023-03-15 15:25:00  2234.65  2234.80  2233.85  2234.35   \n",
       "8246        8246  2023-03-15 15:26:00  2234.35  2234.90  2234.00  2234.60   \n",
       "8247        8247  2023-03-15 15:27:00  2234.65  2235.25  2234.15  2235.15   \n",
       "8248        8248  2023-03-15 15:28:00  2235.00  2238.20  2235.00  2236.10   \n",
       "8249        8249  2023-03-15 15:29:00  2236.00  2237.45  2235.00  2237.45   \n",
       "\n",
       "      Volume  \n",
       "0      40926  \n",
       "1      20289  \n",
       "2      23981  \n",
       "3      31951  \n",
       "4      13916  \n",
       "...      ...  \n",
       "8245   39387  \n",
       "8246   48522  \n",
       "8247   50130  \n",
       "8248   71039  \n",
       "8249   45288  \n",
       "\n",
       "[8250 rows x 7 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f7023b04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2340.20</td>\n",
       "      <td>40926</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2339.40</td>\n",
       "      <td>20289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2340.80</td>\n",
       "      <td>23981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2347.00</td>\n",
       "      <td>31951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2345.00</td>\n",
       "      <td>13916</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8245</th>\n",
       "      <td>2234.65</td>\n",
       "      <td>39387</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8246</th>\n",
       "      <td>2234.35</td>\n",
       "      <td>48522</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8247</th>\n",
       "      <td>2234.65</td>\n",
       "      <td>50130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8248</th>\n",
       "      <td>2235.00</td>\n",
       "      <td>71039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8249</th>\n",
       "      <td>2236.00</td>\n",
       "      <td>45288</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8250 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Open  Volume\n",
       "0     2340.20   40926\n",
       "1     2339.40   20289\n",
       "2     2340.80   23981\n",
       "3     2347.00   31951\n",
       "4     2345.00   13916\n",
       "...       ...     ...\n",
       "8245  2234.65   39387\n",
       "8246  2234.35   48522\n",
       "8247  2234.65   50130\n",
       "8248  2235.00   71039\n",
       "8249  2236.00   45288\n",
       "\n",
       "[8250 rows x 2 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = df.drop(columns=['Unnamed: 0','Time', 'High', 'Low', 'Close'])\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8fb720be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       2339.80\n",
       "1       2340.25\n",
       "2       2345.90\n",
       "3       2345.35\n",
       "4       2344.75\n",
       "         ...   \n",
       "8245    2234.35\n",
       "8246    2234.60\n",
       "8247    2235.15\n",
       "8248    2236.10\n",
       "8249    2237.45\n",
       "Name: Close, Length: 8250, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = df['Close']\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5d5b94c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, shuffle=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4716ca9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9869784591964429"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = LinearRegression()\n",
    "model.fit(x_train, y_train)\n",
    "score = model.score(x_test, y_test)\n",
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f2d3f1e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2297.3653163795752\n",
      "2296.8148482665724\n",
      "2297.3660403113886\n",
      "2298.1660995877037\n",
      "2297.6652890266178\n",
      "2299.6650079184938\n",
      "2298.2163246412224\n",
      "2296.5639517951654\n",
      "2296.411244674174\n",
      "2298.016348589631\n",
      "2297.5568683242122\n",
      "2296.415174745192\n",
      "2298.4655945104823\n",
      "2299.7142998317945\n",
      "2297.415459001174\n",
      "2299.0162851624646\n",
      "2298.116437682946\n",
      "2296.152957079313\n",
      "2290.0999652129367\n",
      "2285.3621947716956\n",
      "2283.7668292490225\n",
      "2286.966516264042\n",
      "2283.5988763035925\n",
      "2281.0611305334996\n",
      "2278.468463538912\n",
      "2279.5614658966438\n",
      "2277.5213751502047\n",
      "2278.517269566373\n",
      "2277.9160992196935\n",
      "2282.512130610216\n",
      "2280.4138047672723\n",
      "2283.466671334199\n",
      "2284.116661038915\n",
      "2282.4713163982206\n",
      "2283.6188593789407\n",
      "2284.0200452404006\n",
      "2282.819546342748\n",
      "2283.9688233863685\n",
      "2284.9197814504296\n",
      "2283.220595905884\n",
      "2283.5708904571507\n",
      "2283.766404302952\n",
      "2280.969744673047\n",
      "2281.9698338673566\n",
      "2283.1708265403727\n",
      "2282.6084811575024\n",
      "2283.96511803075\n",
      "2281.612567153551\n",
      "2282.017329689777\n",
      "2281.8122091246214\n",
      "2282.26614604745\n",
      "2282.8115686740143\n",
      "2280.2127181972055\n",
      "2278.712955621434\n",
      "2279.616232051189\n",
      "2280.5130994671654\n",
      "2280.0134856652107\n",
      "2281.01173279176\n",
      "2283.9657451118587\n",
      "2283.2123040164647\n",
      "2283.212158196302\n",
      "2283.356710542355\n",
      "2285.510743025481\n",
      "2288.007380494781\n",
      "2286.0028906174807\n",
      "2287.508048267207\n",
      "2289.813510584641\n",
      "2291.108764713475\n",
      "2291.46198655009\n",
      "2288.05877755065\n",
      "2289.507509525326\n",
      "2286.462809975702\n",
      "2286.2612399682685\n",
      "2287.6115856264882\n",
      "2286.1658739791305\n",
      "2279.9987221899282\n",
      "2281.8111856629594\n",
      "2283.0136232070245\n",
      "2287.461577538764\n",
      "2292.907965625097\n",
      "2292.0095749869392\n",
      "2293.6088246037502\n",
      "2293.611889819738\n",
      "2289.6100723924033\n",
      "2285.6658958988223\n",
      "2288.012283153636\n",
      "2293.009488707359\n",
      "2295.6555760125684\n",
      "2301.860657168613\n",
      "2297.614946718453\n",
      "2297.8127270339805\n",
      "2302.809523420681\n",
      "2304.0114856889554\n",
      "2303.5597265467236\n",
      "2301.759094910785\n",
      "2298.6132335646735\n",
      "2301.802799408984\n",
      "2301.0096029300867\n",
      "2300.7617172641585\n",
      "2297.1128735615207\n",
      "2300.0652845803593\n",
      "2299.4637717195287\n",
      "2295.0099421410982\n",
      "2298.314905475246\n",
      "2295.36682526082\n",
      "2295.4144285439943\n",
      "2294.3164742858985\n",
      "2294.0166412018098\n",
      "2293.0117744928148\n",
      "2297.8647661338473\n",
      "2297.2665565349794\n",
      "2296.4168884041524\n",
      "2298.716259465177\n",
      "2294.8674824231966\n",
      "2295.268267823315\n",
      "2296.2114941541395\n",
      "2299.811297047973\n",
      "2297.959326031304\n",
      "2298.316998919555\n",
      "2299.1167638350194\n",
      "2299.115561362785\n",
      "2300.8638516484825\n",
      "2298.1150695307138\n",
      "2294.811604389913\n",
      "2294.014713981604\n",
      "2294.0149522996307\n",
      "2295.067021014301\n",
      "2294.6126313960426\n",
      "2294.0146035282723\n",
      "2294.0168855049924\n",
      "2293.66731815017\n",
      "2294.0167611769807\n",
      "2294.0157026205407\n",
      "2295.717629094444\n",
      "2294.3174735348844\n",
      "2294.0153704443874\n",
      "2290.004104632278\n",
      "2285.416718255374\n",
      "2285.965510796772\n",
      "2286.01621738329\n",
      "2286.3108025738484\n",
      "2287.4687651669165\n",
      "2288.617576728638\n",
      "2287.0165761816684\n",
      "2286.567676855755\n",
      "2286.715531919664\n",
      "2287.369220178685\n",
      "2287.718640081029\n",
      "2288.867309359272\n",
      "2289.418866770652\n",
      "2287.519159165064\n",
      "2287.568967978194\n",
      "2286.0195426815076\n",
      "2285.266743086007\n",
      "2285.2699728937823\n",
      "2286.9185808047146\n",
      "2286.319763712521\n",
      "2285.3704480296537\n",
      "2287.968178466148\n",
      "2286.564482958915\n",
      "2288.269540757574\n",
      "2287.8694907154754\n",
      "2288.019275176011\n",
      "2289.81637366559\n",
      "2291.9685858451594\n",
      "2292.0151983129767\n",
      "2293.762033117576\n",
      "2295.514277414915\n",
      "2296.0161413634423\n",
      "2295.714000729695\n",
      "2297.316137640132\n",
      "2293.6140042120924\n",
      "2296.962586619941\n",
      "2293.364776783029\n",
      "2292.0639986273345\n",
      "2291.3693195942187\n",
      "2291.0189273760902\n",
      "2292.4179408590803\n",
      "2289.8674543243524\n",
      "2291.5159931339394\n",
      "2293.564933477508\n",
      "2290.0163236001376\n",
      "2292.6175091039117\n",
      "2292.2622256531354\n",
      "2290.468281340725\n",
      "2290.065063790884\n",
      "2293.1144663127966\n",
      "2291.7154688809064\n",
      "2290.1669897829606\n",
      "2289.0685945276946\n",
      "2289.016731173769\n",
      "2290.0156336748914\n",
      "2290.0082194269717\n",
      "2287.368956559772\n",
      "2287.2191530555588\n",
      "2288.919790816572\n",
      "2288.169695423336\n",
      "2288.2699861075844\n",
      "2288.5696361003124\n",
      "2287.3660776997754\n",
      "2286.019228460822\n",
      "2286.5205820387814\n",
      "2288.1196404026555\n",
      "2289.4182878428433\n",
      "2289.370047956721\n",
      "2287.070060968743\n",
      "2288.762015900834\n",
      "2290.3185091225546\n",
      "2291.9133003423117\n",
      "2288.368591970442\n",
      "2288.070373790242\n",
      "2288.320138523075\n",
      "2288.270320732211\n",
      "2288.320692966155\n",
      "2287.920525941464\n",
      "2288.862494573388\n",
      "2289.012439000818\n",
      "2290.1188021309263\n",
      "2290.4157253410285\n",
      "2291.811868941756\n",
      "2291.3123544389787\n",
      "2290.063158062829\n",
      "2287.106734813105\n",
      "2285.7145784144295\n",
      "2287.567541606718\n",
      "2288.4689822259206\n",
      "2286.620775056167\n",
      "2287.16992126587\n",
      "2285.770835416904\n",
      "2285.318181493862\n",
      "2284.0210050417677\n",
      "2286.32094850134\n",
      "2284.919884558343\n",
      "2283.621532295163\n",
      "2283.7194517694575\n",
      "2283.7684860490017\n",
      "2281.515526681019\n",
      "2280.21473628296\n",
      "2279.8203454778354\n",
      "2282.0178506703946\n",
      "2281.420478177197\n",
      "2280.0722754768485\n",
      "2281.122598974463\n",
      "2281.5723220754735\n",
      "2282.370214453293\n",
      "2282.86943350701\n",
      "2283.869132305922\n",
      "2286.5184885944727\n",
      "2286.06848364703\n",
      "2284.618971425664\n",
      "2285.719663348487\n",
      "2286.520098329362\n",
      "2286.0191356909054\n",
      "2286.319311833249\n",
      "2286.2212677588896\n",
      "2286.170059779538\n",
      "2287.5165967021735\n",
      "2285.9206280390154\n",
      "2286.020553900805\n",
      "2285.07065711371\n",
      "2286.9694824529047\n",
      "2288.3640620235697\n",
      "2292.0151716518276\n",
      "2290.868290846994\n",
      "2292.667116598161\n",
      "2292.9145922809084\n",
      "2295.9634827999375\n",
      "2297.506587499922\n",
      "2298.463338922859\n",
      "2298.7577548967365\n",
      "2298.6064804044304\n",
      "2299.554859954501\n",
      "2302.013153176832\n",
      "2299.4150334331507\n",
      "2297.26662835685\n",
      "2296.1651738707524\n",
      "2296.3132014159733\n",
      "2295.0645249322306\n",
      "2297.800096178573\n",
      "2294.1641915668724\n",
      "2292.3162874636505\n",
      "2292.116907207125\n",
      "2291.717766636674\n",
      "2291.4140453776595\n",
      "2289.217777752112\n",
      "2288.0120184465127\n",
      "2285.013856006152\n",
      "2282.254861852124\n",
      "2287.0132345602983\n",
      "2284.269665513334\n",
      "2283.6662564462886\n",
      "2285.0651847768327\n",
      "2283.2198850325926\n",
      "2285.0180360934555\n",
      "2286.170135410144\n",
      "2285.0173339258454\n",
      "2288.656502895994\n",
      "2284.1666981041276\n",
      "2285.1131354711024\n",
      "2288.095543076719\n",
      "2284.7701036344906\n",
      "2283.0089468958845\n",
      "2286.468883004591\n",
      "2285.3499279225884\n",
      "2281.9173679170517\n",
      "2283.969496172304\n",
      "2283.269926994751\n",
      "2285.5064097725963\n",
      "2288.013977224813\n",
      "2289.445011637544\n",
      "2282.1598538841313\n",
      "2282.3197646843746\n",
      "2281.6710231567204\n",
      "2281.1215012424573\n",
      "2281.1716634518393\n",
      "2281.0159028131197\n",
      "2279.7183604503566\n",
      "2277.5153646934004\n",
      "2279.221506349385\n",
      "2280.8718192135966\n",
      "2280.2713640930488\n",
      "2280.019223525368\n",
      "2279.020680677706\n",
      "2278.0221198745758\n",
      "2279.2211298286675\n",
      "2279.9718871257373\n",
      "2280.521413120788\n",
      "2281.369220684282\n",
      "2283.3195295920546\n",
      "2284.1699213826423\n",
      "2283.7677580363998\n",
      "2285.0196675925486\n",
      "2283.1199806629534\n",
      "2280.020279633335\n",
      "2280.6123354037095\n",
      "2285.059388697431\n",
      "2281.3453263095416\n",
      "2286.0471460220765\n",
      "2281.9530114984386\n",
      "2280.7704098492964\n",
      "2281.0717577219375\n",
      "2281.0708297507176\n",
      "2280.919762562448\n",
      "2279.321059771246\n",
      "2280.3220451066277\n",
      "2281.7676452124433\n",
      "2281.7701557132987\n",
      "2281.469597065081\n",
      "2281.0168318725496\n",
      "2277.1187694465298\n",
      "2276.7180218617145\n",
      "2276.2561129832557\n",
      "2271.712707509932\n",
      "2272.020620282458\n",
      "2272.072338360326\n",
      "2273.2675738574535\n",
      "2270.123067333\n",
      "2272.072356587846\n",
      "2272.023663190137\n",
      "2272.972577867557\n",
      "2272.0221051452304\n",
      "2273.9216857022816\n",
      "2274.6174102333152\n",
      "2275.6226956311716\n",
      "2274.4229209373852\n",
      "2274.222010385313\n",
      "2273.170482511096\n",
      "2272.173332028342\n",
      "2273.822955783465\n",
      "2274.571847344204\n",
      "2274.421325349228\n",
      "2274.6215998424577\n",
      "2274.519297873768\n",
      "2275.421715433649\n",
      "2275.272079241749\n",
      "2274.720320511488\n",
      "2276.121511230969\n",
      "2275.8667284890034\n",
      "2277.5670762420073\n",
      "2279.1216354422086\n",
      "2277.12167333536\n",
      "2278.171998737343\n",
      "2279.6212718245247\n",
      "2278.4222762892177\n",
      "2279.01619425924\n",
      "2279.464992925713\n",
      "2283.018548990345\n",
      "2281.769553388971\n",
      "2281.7193919957467\n",
      "2282.5186604153228\n",
      "2282.567337761932\n",
      "2280.870436914632\n",
      "2280.2208566489912\n",
      "2278.7210918968\n",
      "2277.9704319945395\n",
      "2277.4209288519028\n",
      "2277.8200884660314\n",
      "2277.47036277663\n",
      "2276.6210183883277\n",
      "2276.5210128151434\n",
      "2276.2698217108336\n",
      "2276.922041430234\n",
      "2276.771231059564\n",
      "2275.822105541424\n",
      "2276.3717681068506\n",
      "2276.5164861329013\n",
      "2275.221050817074\n",
      "2275.019926975809\n",
      "2275.072126586676\n",
      "2275.922132334707\n",
      "2275.5214478660814\n",
      "2275.4206424584245\n",
      "2275.0196881136776\n",
      "2275.5214241975104\n",
      "2275.7220129114257\n",
      "2275.019454692597\n",
      "2275.4213263985143\n",
      "2275.019650842479\n",
      "2275.0710114433077\n",
      "2276.219238364117\n",
      "2276.3657636352023\n",
      "2276.5207693281186\n",
      "2275.517904109673\n",
      "2275.0693677018503\n",
      "2273.8203016388684\n",
      "2273.5709800796253\n",
      "2273.7176598765536\n",
      "2274.2217113995694\n",
      "2273.920295785846\n",
      "2275.0678841993404\n",
      "2276.8193471617797\n",
      "2274.9702544610022\n",
      "2275.7695751146666\n",
      "2275.719119904697\n",
      "2276.01720559531\n",
      "2278.166265230026\n",
      "2277.0184697845475\n",
      "2275.417642807099\n",
      "2276.016312174763\n",
      "2276.4688872025677\n",
      "2276.4600767810034\n",
      "2276.617893864886\n",
      "2276.969745644901\n",
      "2277.6705782344584\n",
      "2277.4144205389466\n",
      "2276.365850419963\n",
      "2276.416458251408\n",
      "2276.515740164832\n",
      "2276.9150877672673\n",
      "2276.8693056038073\n",
      "2284.069740137042\n",
      "2294.399609336865\n",
      "2294.504539061055\n",
      "2296.854864820515\n",
      "2289.1103418799075\n",
      "2293.2611074782644\n",
      "2291.0414732599083\n",
      "2293.0565299299824\n",
      "2292.0148296817824\n",
      "2290.0125907672123\n",
      "2286.563869480434\n",
      "2284.6513022232502\n",
      "2284.018714631419\n",
      "2284.615731551944\n",
      "2289.261918622588\n",
      "2289.910217520757\n",
      "2287.368457887463\n",
      "2286.9672676731625\n",
      "2286.8165590501435\n",
      "2286.517471662072\n",
      "2287.0138175688953\n",
      "2286.668077177178\n",
      "2284.062399269782\n",
      "2282.9029561667817\n",
      "2278.919558056785\n",
      "2280.2172723567537\n",
      "2279.3177717442263\n",
      "2280.2396552810997\n",
      "2277.920483346403\n",
      "2279.020858055963\n",
      "2280.0176102537957\n",
      "2278.5210913604797\n",
      "2279.720422608623\n",
      "2281.368737518968\n",
      "2279.917729552728\n",
      "2281.819588549816\n",
      "2280.6199188683104\n",
      "2279.0657391814048\n",
      "2277.468760931264\n",
      "2276.2185563283947\n",
      "2277.215318320119\n",
      "2275.3633443108724\n",
      "2275.0153170454896\n",
      "2277.368118755132\n",
      "2275.0116089693456\n",
      "2275.520836291968\n",
      "2273.618560238333\n",
      "2276.020330662857\n",
      "2276.965268204169\n",
      "2275.7205966058937\n",
      "2276.6154628033732\n",
      "2272.6189615547564\n",
      "2274.7164576374475\n",
      "2273.361290936136\n",
      "2281.706354149737\n",
      "2275.0696234312395\n",
      "2275.9218447751705\n",
      "2275.520958443559\n",
      "2275.4731581943443\n",
      "2275.2195735717723\n",
      "2276.5227746274036\n",
      "2275.021668928234\n",
      "2275.567142972728\n",
      "2278.916808693798\n",
      "2275.671594972655\n",
      "2276.271192311539\n",
      "2276.118470227658\n",
      "2277.46666367822\n",
      "2276.8571883835984\n",
      "2276.4719741827585\n",
      "2276.271596853668\n",
      "2276.369475792134\n",
      "2277.905927719263\n",
      "2280.004263628151\n",
      "2277.9130239377614\n",
      "2276.6193849848673\n",
      "2278.4178976035587\n",
      "2276.6213666155813\n",
      "2276.2208083793353\n",
      "2275.5628151608944\n",
      "2274.968343563949\n",
      "2276.073213669709\n",
      "2275.020466455999\n",
      "2274.0731707632553\n",
      "2274.673904465606\n",
      "2274.172433088896\n",
      "2273.022804825444\n",
      "2273.9205561401286\n",
      "2272.1187949420364\n",
      "2270.371487854225\n",
      "2270.3712653152456\n",
      "2270.923548018702\n",
      "2270.1643385932657\n",
      "2267.5232657605056\n",
      "2267.473084507446\n",
      "2267.875191538812\n",
      "2268.0708188305243\n",
      "2267.0690001982066\n",
      "2265.017654910169\n",
      "2263.268523710065\n",
      "2264.973857642053\n",
      "2265.225095267348\n",
      "2265.124992027301\n",
      "2265.225509603369\n",
      "2266.924853210441\n",
      "2267.623893517853\n",
      "2266.425363192393\n",
      "2265.767978011382\n",
      "2264.2234551014976\n",
      "2265.2254723321707\n",
      "2265.4256668419534\n",
      "2265.075087451676\n",
      "2265.175833823932\n",
      "2265.223391402279\n",
      "2265.1740733719344\n",
      "2266.324688642008\n",
      "2267.321163618301\n",
      "2269.822687967408\n",
      "2269.2250222015705\n",
      "2267.9243732708337\n",
      "2266.523378701235\n",
      "2265.7758955565046\n",
      "2266.5751005878383\n",
      "2266.2747644786\n",
      "2268.023830930199\n",
      "2268.1615925727574\n",
      "2268.4090356092\n",
      "2266.7245267551757\n",
      "2266.525651428168\n",
      "2267.3750747117074\n",
      "2267.6736786624124\n",
      "2268.0553300631655\n",
      "2265.4118781309285\n",
      "2268.2186885852702\n",
      "2269.7236674964765\n",
      "2270.022157729219\n",
      "2270.5223055703136\n",
      "2270.4694416071397\n",
      "2270.817241980704\n",
      "2272.2212478998863\n",
      "2270.9741207553693\n",
      "2270.473025355272\n",
      "2270.673498174805\n",
      "2271.9243252338897\n",
      "2271.5607164312314\n",
      "2277.760166371715\n",
      "2272.665107180412\n",
      "2273.2174603454764\n",
      "2276.2191423295694\n",
      "2275.72127374467\n",
      "2275.6213340082004\n",
      "2275.117216376417\n",
      "2276.217606320919\n",
      "2276.7200255286843\n",
      "2277.2222921149737\n",
      "2276.017519815996\n",
      "2275.6703579497475\n",
      "2276.971813244218\n",
      "2275.070545145251\n",
      "2274.9196308505097\n",
      "2274.9711927702187\n",
      "2274.9200688551023\n",
      "2274.2698076419497\n",
      "2272.522735607534\n",
      "2273.1220021305267\n",
      "2272.5722799855935\n",
      "2271.1225343431465\n",
      "2273.068827755403\n",
      "2273.023099186294\n",
      "2273.6231584703933\n",
      "2273.022546375529\n",
      "2270.919175318199\n",
      "2270.423551438821\n",
      "2270.272776434981\n",
      "2270.9633842018097\n",
      "2270.520539949318\n",
      "2271.0737503519417\n",
      "2271.173415315344\n",
      "2271.271045325734\n",
      "2269.7232942403894\n",
      "2268.022688309524\n",
      "2268.973668137788\n",
      "2269.122737372191\n",
      "2269.31989278303\n",
      "2271.671555680733\n",
      "2270.823067713832\n",
      "2268.3736045008477\n",
      "2268.174351020807\n",
      "2269.3242154258655\n",
      "2269.4222850731635\n",
      "2270.511482504046\n",
      "2270.81562109166\n",
      "2267.7133529742578\n",
      "2267.7731251676237\n",
      "2268.5739995133536\n",
      "2268.473853016952\n",
      "2268.1682902342827\n",
      "2267.1246371929383\n",
      "2266.3749925907637\n",
      "2267.0136001612386\n",
      "2266.473837859858\n",
      "2266.1754744036\n",
      "2265.970068999433\n",
      "2265.911981083353\n",
      "2265.7753528116837\n",
      "2265.774934122822\n",
      "2267.473849519193\n",
      "2266.0741379493816\n",
      "2266.3249223351413\n",
      "2266.8239153131963\n",
      "2267.722709949378\n",
      "2268.4241152095356\n",
      "2268.9743779228693\n",
      "2268.62447050237\n",
      "2268.024768423258\n",
      "2267.6731408145374\n",
      "2267.0235839454153\n",
      "2267.122476279599\n",
      "2265.7240074457977\n",
      "2265.5170197840484\n",
      "2264.974967344371\n",
      "2265.075224294105\n",
      "2264.574612603427\n",
      "2264.5747350270703\n",
      "2264.6073590972965\n",
      "2264.2175537377625\n",
      "2260.3184188806235\n",
      "2260.750141081104\n",
      "2258.0233533231244\n",
      "2258.223841921704\n",
      "2259.6734444645144\n",
      "2260.823253370854\n",
      "2260.072981143466\n",
      "2259.9247446618933\n",
      "2259.169242496443\n",
      "2255.722886706514\n",
      "2257.475570368708\n",
      "2257.773074955092\n",
      "2256.3260305223325\n",
      "2255.2697844408835\n",
      "2253.6263161465695\n",
      "2254.5704119573184\n",
      "2252.075454684516\n",
      "2252.126918121204\n",
      "2251.9249041240228\n",
      "2253.075662765786\n",
      "2253.97548412826\n",
      "2253.024763838121\n",
      "2251.073756843527\n",
      "2250.6665251584323\n",
      "2252.725769219966\n",
      "2251.626011525571\n",
      "2252.027138079577\n",
      "2251.72478986974\n",
      "2252.425465757033\n",
      "2253.0251847034033\n",
      "2252.577423917377\n",
      "2252.275488411246\n",
      "2252.316942292294\n",
      "2254.120752516603\n",
      "2254.6256155723504\n",
      "2255.1260077166276\n",
      "2255.726589341607\n",
      "2255.0259341303076\n",
      "2254.927363906333\n",
      "2253.027458518547\n",
      "2253.4752889500237\n",
      "2254.375407393874\n",
      "2254.0268556111905\n",
      "2253.425404506287\n",
      "2256.4761604895953\n",
      "2256.3269418983473\n",
      "2254.4763107404465\n",
      "2256.12681431349\n",
      "2255.1263336355723\n",
      "2254.025319058435\n",
      "2253.577084900986\n",
      "2253.4770344391313\n",
      "2252.726372360451\n",
      "2252.2118628656785\n",
      "2253.068909877595\n",
      "2253.024774720223\n",
      "2252.574723251795\n",
      "2250.5227914184775\n",
      "2250.8790575230346\n",
      "2251.3279609297365\n",
      "2250.7279288508907\n",
      "2251.77824962798\n",
      "2250.62863551126\n",
      "2251.078754720771\n",
      "2251.7274342204455\n",
      "2251.878550378173\n",
      "2251.8779124149623\n",
      "2253.2271026660374\n",
      "2253.8775611172828\n",
      "2254.524382226045\n",
      "2256.9253408457844\n",
      "2256.8752648770583\n",
      "2256.9258011586853\n",
      "2255.027365126677\n",
      "2256.0753174143383\n",
      "2257.0242266507075\n",
      "2258.425074039881\n",
      "2258.1773720094193\n",
      "2258.0756761737925\n",
      "2258.974320909024\n",
      "2256.725486945784\n",
      "2255.6756574955853\n",
      "2254.978556922795\n",
      "2254.0283391137004\n",
      "2253.6271070033085\n",
      "2254.728369692364\n",
      "2254.3274904341197\n",
      "2253.828260498301\n",
      "2253.8762174497792\n",
      "2252.0782111208687\n",
      "2253.1732465272444\n",
      "2253.029129737311\n",
      "2253.876304778645\n",
      "2254.9778729827053\n",
      "2252.927076696697\n",
      "2252.0262963490127\n",
      "2251.1772874014946\n",
      "2251.4746962253835\n",
      "2251.2254190107046\n",
      "2250.025092322311\n",
      "2250.1771807958226\n",
      "2250.077993284631\n",
      "2250.120379416212\n",
      "2250.5278700953268\n",
      "2251.027715686047\n",
      "2250.778391678331\n",
      "2250.0777585032874\n",
      "2250.6723925155998\n",
      "2250.078772171058\n",
      "2250.178466788187\n",
      "2250.8791424034275\n",
      "2250.428374620658\n",
      "2250.128934652492\n",
      "2250.325639272269\n",
      "2250.077713070513\n",
      "2250.067670250935\n",
      "2245.5787101822107\n",
      "2246.327906985901\n",
      "2246.1265872668055\n",
      "2246.623333907023\n",
      "2245.122968190767\n",
      "2243.9238589374977\n",
      "2245.8746216289096\n",
      "2246.9768887359496\n",
      "2246.376534818947\n",
      "2245.024840052173\n",
      "2243.1743081934505\n",
      "2242.0232633524133\n",
      "2241.4272644524995\n",
      "2241.676271519004\n",
      "2241.019867359459\n",
      "2240.171411222706\n",
      "2236.915496042781\n",
      "2235.5753550754016\n",
      "2235.524551094074\n",
      "2236.521877594822\n",
      "2232.976776379082\n",
      "2230.112325263038\n",
      "2229.9762432728726\n",
      "2231.0089347732055\n",
      "2232.3741007656886\n",
      "2235.92665812544\n",
      "2236.9778010453106\n",
      "2237.12596760938\n",
      "2234.676599886838\n",
      "2234.374204067806\n",
      "2234.673677226382\n",
      "2235.017884602027\n",
      "2236.0245922905715\n"
     ]
    }
   ],
   "source": [
    "predict = model.predict(x_test)\n",
    "for i in predict:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1bd34d0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d075b43c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae6f933a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc7e6f81",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
