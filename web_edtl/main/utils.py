import hashlib
import re




def title_seo(title):
    result = re.sub('[\W_]+', '-', title)
    return result.lower()

def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()


def get_client_ip(request):
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward_for:
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
# def hash_md5(strhash):
#     hashed = hashlib.md5(strhash.encode())
#     return hashed.hexdigest()

# def getjustnewid(table_name):
#     result = table_name.objects.last()
#     if result:
#         newid = result.id + 1
#     else:
#         newid = 1
#     return newid
