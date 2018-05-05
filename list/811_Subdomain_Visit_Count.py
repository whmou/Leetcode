class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        tmp_dict = {}
        for cpd in cpdomains:
            cnt, url = cpd.split()
            cnt = int(cnt)
            tmp_sub_ds = url.split('.')[::-1]

            sub_ds = []
            for i, domain in enumerate(tmp_sub_ds):
                sub_ds.append('.'.join(tmp_sub_ds[:i + 1][::-1]))

            for sub_d in sub_ds:
                if sub_d not in tmp_dict:
                    tmp_dict[sub_d] = cnt
                else:
                    tmp_dict[sub_d] += cnt
        result = []
        for k in tmp_dict:
            result.append('{0} {1}'.format(tmp_dict[k], k))
        return result
