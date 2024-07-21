from django import template

register=template.Library()
@register.filter(name='chunks')
def chunks(list_item,chunk_size):
    i=0
    chunk=[]
    for data in list_item:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk
            chunk=[]
            i=0
    yield chunk
            
    