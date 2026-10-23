

def cala_data(*args,**kwargs):
    min_v=min(args)
    max_v=max(args)
    avg_v=sum(args)/len(args)

    if kwargs.get('round'):
        avg_v=round(avg_v,kwargs.get('round'))

    return min_v,max_v,avg_v

if __name__ == '__main__':
    res=cala_data(1,2,3,4,5,6,7,300,3,2,round=3,count=0)
    print(res)