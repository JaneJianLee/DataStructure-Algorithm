#811. Subdomain Visit Count

#join and split functions : string <--> list
#join function takes only one argument
# use a dictionary to make key, value
# function + for in loop...


class Solution:
    def subdomainVisits(self, pdomaicns: List[str]) -> List[str]:
        dict={}
        for domain in pdomaicns:
            count, address = domain.split()
            count=int(count)
            frag=address.split(".")
            for i in range(len(frag)):
                sub = '.'.join(frag[i:])
                dict[sub] = dict.get(sub,0)+count

        return [' '.join([str(v),k]) for k, v in dict.items()]
