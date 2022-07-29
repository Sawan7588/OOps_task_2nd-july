import logging
logging.basicConfig(filename="log_file.log", level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class string_data:

    def __init__(self,s):
        self.s = s

    def extract_jump(self):
        """ This function helps to jump the string """
        logging.info("in string class")
        try:
            logging.info("Try to extract data from index one to index 300 with a jump of 3")
            return self.s[1:300:3]
        except Exception as e:
            logging.exception(e)

    def reverse_string(self):
        """ This function reverse the string without using reverse function """
        try:
            logging.info("Try to reverse a string without using reverse function")
            return self.s[::-1]
        except Exception as e:
            logging.exception(e)

    def split_string(self):
        """ This function helps to split string """
        try:
            logging.info("Try to split a string after conversion of entire string in uppercase")
            return ((self.s).upper()).split()
        except Exception as e:
            logging.exception(e)

    def lower_string(self):
        """ This function helps to convert string into lower case """
        try:
            logging.info("try to convert the whole string into lower case")
            return (self.s).lower()
        except Exception as e:
            logging.exception(e)

    def capitalize_string(self):
        """ This function helps to capitalize the string """
        try:
            logging.info("Try to capitalize the whole string")
            return (self.s).capitalize()
        except Exception as e:
            logging.exception(e)

class list_extraction:

    def __init__(self, data):
        self.data = data

    def extract_list(self):
        """ This function extract only list out of whole data """
        logging.info(" in list class ")
        try:
            logging.info("accessing list function to extract list entity")
            a = []
            for i in self.data:
                if type(i) == list:
                    a.append(i)
            logging.info("list entity extracted ")
            return a

        except Exception as e:
            logging.exception(e)

    def list_numeric_data(self):
        """ This function extracts list numeric data """
        try:
            logging.info("accessing list numeric data function")
            n = []
            for i in self.data:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            n.append(j)
            logging.info("numeric data extracted")
            return n
        except Exception as e:
            logging.exception(e)

    def multiplication_list(self):
        """ This function multiply only list elements """
        try:
            logging.info("accessing multiplication of list function")
            m = []
            prod = 1
            for i in self.data:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            m.append(j)
                            prod = prod * j
            logging.info("multiplication done of all list elements")
            return ("multiplication of all list elements :-  ", prod)

        except Exception as e:
            logging.exception(e)

    def sum_list_numeric_data(self):
        """ This function used to calculate only sum of list numeric data"""
        try:
            logging.info("accessing sum of list numeric data function")
            l1 = []
            for i in self.data:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
            logging.info("sumation done of all list elements")
            return sum(l1)

        except Exception as e:
            logging.exception(e)

class tuple_extraction(list_extraction):
    


    def extract_tuple(self):
        """ This function used to extract tuple elements """
        logging.info("inheriting attributes of list class into tuple class")
        try:
            output = []
            logging.info(" accessing extract tuple function ")
            for i in self.data:
                if type(i) == tuple:
                    output.append(i)
            logging.info("tuple elements extracted out of whole list")
            return output
        except Exception as e:
            logging.exception(e)

    def tuple_numeric_data(self):
        """ This function used to extract tuple numeric data """
        
        try:
            logging.info("accessing tuple numeric data function")
            output = []
            for i in self.data:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
            logging.info("tuple numeric data extracted")
            return output

        except Exception as e:
            logging.exception(e)

    def multiplication_tuple(self):
        """ This function used to do multiplication of tuple data """
        try:
            logging.info("accessing multiplication of tuple function")
            output = []
            prod = 1
            for i in self.data:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            prod = prod * j
            logging.info("multiplication of all tuple elements done ")
            return prod

        except Exception as e:
            logging.exception(e)

    def sum_tuple_numeric_data(self):
        """ This function used to do summation of tuple numeric data """ 
        try:
            logging.info("accessing tuple sum of numeric data function")
            output = []
            for i in self.data:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
            logging.info(" summation of tuple numeric data done ")
            return sum(output)

        except Exception as e:
            logging.exception(e)

class dict_extraction(tuple_extraction):


    def extract_dict(self):
        """ This function used to extract dict elements """
        logging.info("inheriting tuple class attributes into dict class")
        try:
            logging.info("accessing dict extract function")
            for i in self.data:
                if type(i) == dict:
                    logging.info("dict elements extracted")
                    return i
        except Exception as e:
            logging.exception(e)

    def dict_numeric_data(self):
        """ This function used to extract dict numeric data """
        try:
            logging.info("accessing dict numeric data function")
            output = []
            for i in self.data:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            output.append(i[j])
            logging.info(" dict numeric data extracted ")
            return output

        except Exception as e:
            logging.exception(e)

    def num_keys(self):
        """ This function used to find num of keys of dict out of whole data """
        try:
            logging.info("accessing num of keys function")
            output = []
            for i in self.data:
                if type(i) == dict:
                    for j, k in i.items():
                        output.append(j)
            logging.info(" number of keys extracted ")
            return ("number of keys ", len(output))

        except Exception as e:
            logging.exception(e)

    def multiplication_dict(self):
        """ This function used to find multiplication of dict elements """
        try:
            logging.info("accessing dict multiplication function")
            output = []
            prod = 1
            for i in self.data:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            output.append(i[j])

            for i in output:
                prod = prod * i
            logging.info(" multiplication of dict elements done ")
            return ("multiplication of dict elements :- ", prod)

        except Exception as e:
            logging.exception(e)

    def sum_dict_numeric_data(self):
        """ This function used to find summation of dict numeric elements """
        try:
            logging.info("accessing dict numeric data sum function")
            output = []
            for i in self.data:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            output.append(i[j])
            logging.info(" summation of dict numeric elements done ")
            return sum(output)

        except Exception as e:
            logging.exception(e)
            
class all_data(dict_extraction):


    def all_numeric_data(self):
        """ This function used to extract numeric data """
        logging.info("inheriting dict class attributes into all data class")
        try:
            logging.info("accessing all numeric data function")
            output = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
            for i in self.data:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            output.append(i[j])
            logging.info(" all numeric data extracted ")
            return ("all numeric data in whole list :- ",output)
            
        except Exception as e:
            logging.exception(e)

    def odd_value_all_data(self):
        """ This function used to find odd values out of data """
        try:
            logging.info("accessing odd value data function")
            output = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
            for i in self.data:
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            output.append(j)
                            output.append(i[j])

            output1 = []
            for i in output:
                if i % 2 != 0:
                    output1.append(i)
            logging.info(" odd values extracted out of data ")
            return output1

        except Exception as e:
            logging.exception(e)

    def ineuron(self):
        """ This function used to extract ineuron from the data """
        try:
            logging.info("accessing ineuron function")
            output = []
            for i in self.data:
                # first extracting "ineuron" from dict
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str and j == "ineuron":
                            return j

                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == str and key == "ineuron":
                            output.append(key)
                        if type(val) == str and key == "ineuron":
                            output.append(val)
            logging.info(" extracted ineuron from the data ")
            return output
        except Exception as e:
            logging.exception(e)

    def occurences(self):
        """ This function used to find num of occurences of elements """
        try:
            logging.info("accessing occurences function")
            output = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            output.append(j)
                if type(i) == dict:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            output.append(j)
                            output.append(i[j])
            for i in set(output):
                logging.info("found num of occurences of all elements")
                return ("number of occurences of ", i, output.count(i))
        except Exception as e:
            logging.exception(e)

    def unwrape_data(self):
        """ This function used to Unrape list of all the collection of data  """
        try:
            logging.info("accessing unwrape all data function")
            output = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            output.append(j)
                if type(i) == dict:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            output.append(j)
                            output.append(i[j])

            logging.info("Unrape done list of all the collection of data ")
            return ("Unrape list of all the collection of data :- ", output)

        except Exception as e:
            logging.exception(e)

class pattern:


    def Print_pattern1(self):
        """ This function used to print the triangular pattern """
        logging.info("in pattern class")
        try:
            logging.info("accessing pattern1 function")
            n = 4
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print("ineuron", end="  ")
                print(" ")



            logging.info(" triangular pattern printed ")

        except Exception as e:
            logging.exception(e)

    def Print_pattern2(self):
        """ This function used to print diamond pattern """
        try:
            logging.info("accessing pattern2 function")
            n = 4
            for i in range(n - 1):
                for j in range(i, n):
                    print(" " * (len("ineuron") - 1), end=" ")
                for j in range(i):
                    print("ineuron", end=" ")
                for j in range(i + 1):
                    print("ineuron", end=" ")
                print()

            for i in range(n):
                for j in range(i + 1):
                    print(" " * (len("ineuron") - 1), end=" ")
                for j in range(i, n - 1):
                    print("ineuron", end=" ")
                for j in range(i, n):
                    print("ineuron", end=" ")
                print()
            logging.info(" Diamond pattern printed")

        except Exception as e:
            logging.exception(e)


s = string_data("this is My First Python programming class and i am learNING python string and its function")

data = all_data([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 5, 45, 45, 4, 5]),
                          {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "datascience"]])

# performing string actions



logging.info("data from index one to index 300 with a jump of 3 :- %s",(s.extract_jump()))
logging.info("Reverse of string :- %s",(s.reverse_string()))
logging.info("lower case string :- %s",(s.lower_string()))
logging.info("Conversion and split of string in uppercase :- %s",(s.split_string()))
logging.info("capitalize of string :- %s",(s.capitalize_string()))

# list actions

print(" ******** List actions ******** ")


print("all the list entity :-  ",(data.extract_list()))
print("list numeric entity :-  ",(data.list_numeric_data()))
print("multiplication of list entity :-  ",(data.multiplication_list()))
print("sum of list numeric entity :-  ",(data.sum_list_numeric_data()))

# Tuple actions
print(" ******* All tuple action *******")

print("all the tuple entity :-  ",(data.extract_tuple()))
print("tuple numeric entity :-  ",(data.tuple_numeric_data()))
print("multiplication of tuple entity :-  ",(data.multiplication_tuple()))
print("sum of tuple entity :-  ",(data.sum_tuple_numeric_data()))

# dict actions
print(" ****** All dict actions ******** ")

print("all the dict entity :-  ",(data.extract_dict()))
print("dict numeric entity :-  ",(data.dict_numeric_data()))
print("number of keys in dict :-  ",(data.num_keys()))
print("multiplication of dict elements :-  ",(data.multiplication_dict()))
print("sum of dict elements :-  ",(data.sum_dict_numeric_data()))

# all data actions
print(" ******* All data action ******* ")

print("extracting all numeric data :-  ",(data.all_numeric_data()))
print("extracting odd values out of all data :-  ",(data.odd_value_all_data()))
print("extracting ineuron out of all data :-  ",(data.ineuron()))
print("number of occurences of all data :-  ",(data.occurences()))
print("unwrape of all data :-  ",(data.unwrape_data()))


# print patterns
print(" ***** Pattern ***** ")

p = pattern() # calling pattern class
print(p.Print_pattern1())
print(p.Print_pattern2())