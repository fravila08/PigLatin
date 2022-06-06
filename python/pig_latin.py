from operator import index
from xxlimited import new


def translate(word_or_phrase):
      word=word_or_phrase.split()
      vowels_lower=['a','e','i','o','u']
      vowels_upper=[x.upper() for x in vowels_lower]
      answer=[]
      #print(word)
      for i in word:
        filter=''
        if i[len(i)-1].isalnum()!= True:
          filter+=i[len(i)-1]
          i=i.replace(i[len(i)-1], '')         
        if i[0] in vowels_lower:
            for j in vowels_lower:
                if i[0]== j:
                    i+='ay'+ filter
                    answer.append(i)
        elif i[0] in vowels_upper:
            for k in vowels_upper:
                if i[0]== k:
                      i+='ay'+ filter
                      answer.append(i)
        else:
              if i[0]==i[0].upper():
                    alter=[]
                    
                    for j in i:
                        alter.append(j)
                    alter[0]= alter[0].lower()
                    alter[1]=alter[1].upper()
                    alter= ''.join(alter)
                    new_str=alter[1:]+alter[0]
                    answer.append(new_str+ 'ay' + filter)
              else:
                    #print(i)
                    push=''
                    holder=''
                    for x in i:
                          #print(x)
                          for y in i[1:]:
                                if x=='q' and y=='u':
                                      push+=(i[:i.index(y)+1])
                                      holder+=i[i.index(y)+1:]
                                      if push == 'ssqu':
                                        push=push[1:]
                                      return holder + push+ 'ay'
                          #print(x in vowels_lower)
                          if(x in vowels_lower) == False:
                                push=push + x  
                          if (x in vowels_lower) == True:
                                holder+= i[i.index(x):]
                                break
                    #print('hi')
                    answer.append(holder + push +'ay' + filter)
        
      return ' '.join(answer)
        #print(i[0] in vowels_lower, i[0] in vowels_upper)
        
              

print(translate('the quick brown fox'))