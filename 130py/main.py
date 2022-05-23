import pandas as pd
#read csv file
df = pd.read_csv("final.csv")
#check number of rows and columns
print(df.shape)
print(df.columns)

df.drop(columns=['hyperlink', 'temp_planet_date','temp_planet_mass','pl_letter', 'pl_name', 'pl_controvflag', 'pl_pnum', 'pl_orbper', 'pl_orbpererr1','pl_orbpererr2', 'pl_orbperlim', 'pl_orbsmax', 'pl_orbsmaxerr1','pl_orbsmaxerr2', 'pl_orbsmaxlim', 'pl_orbeccen', 'pl_orbeccenerr1','pl_orbeccenerr2', 'pl_orbeccenlim',  'pl_orbinclerr1','pl_orbinclerr2', 'pl_orbincllim', 'pl_bmassj', 'pl_bmassjerr1','pl_bmassjerr2', 'pl_bmassjlim', 'pl_bmassprov', 'pl_radj','pl_radjerr1', 'pl_radjerr2', 'pl_radjlim',  'pl_denserr1','pl_denserr2', 'pl_denslim', 'pl_ttvflag', 'pl_kepflag', 'pl_k2flag','pl_nnotes', 'ra',  'dec', 'st_dist', 'st_disterr1','st_disterr2', 'st_distlim', 'gaia_dist', 'gaia_disterr1','gaia_disterr2', 'gaia_distlim', 'st_optmag', 'st_optmagerr','st_optmaglim', 'st_optband', 'gaia_gmag', 'gaia_gmagerr','gaia_gmaglim',  'st_tefferr1', 'st_tefferr2', 'st_tefflim', 'st_masserr1', 'st_masserr2', 'st_masslim', 'st_raderr1', 'st_raderr2', 'st_radlim', 'rowupdate', 'pl_facility'],inplace=True)
#check number of rows and columns
print(df.shape)
print(df.columns)

#Rename column headers
df = df.rename({
    'pl_hostname': "solar_system_name", 'pl_discmethod': "planet_discovery_method", 'pl_orbincl': "planet_orbital_inclination", 'pl_dens': "planet_density", 'ra_str': "right_ascension", 'dec_str': "declination", "st_teff": "host_temperature", 'st_mass': "host_mass", 'st_rad': "host_radius"
},axis="columns")
print(df.columns)
#Save the data into main.csv
df.to_csv("exo_planets.csv")
