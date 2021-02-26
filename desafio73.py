times = ('flamengo', 'corinthians', 'vasco', 'sport', 'náutico', 'santa cruz', 'central', 'botafogo', 'palmeiras', 'cruzeiro', 'salgueiro', 'íbis', 'são paulo', 'américa', 'bahia','ferroviário', 'atlético-MG', 'vitória', 'fluminense', 'petrolina social')
for time in times[:5]:
    print(f'{time} na {times.index(time) + 1}° posição')
print('\n')
for time in times[16:]:
    print(f'{time} na {times.index(time) + 1}° posição')
print('\ntimes organizados por nome\n')
for time in sorted(times):
    print(f'{time}')
