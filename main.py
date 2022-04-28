""" Leetcode Q 20 :
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
"""

import datetime
import logging

format_used = logging.Formatter('%(asctime)s - %(lineno)d - %(message)s', datefmt='%D %I:%M:%S %p')
log = logging.getLogger()
log.setLevel(logging.INFO)

streamer = logging.StreamHandler()
streamer.setFormatter(format_used)
streamer.setLevel(logging.INFO)
log.addHandler(streamer)

ts = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%Y')
file_handler = logging.FileHandler(f'Result_{ts}.log')
file_handler.setFormatter(format_used)
file_handler.setLevel(logging.INFO)
log.addHandler(file_handler)

log.propagate = False


class ValidBrackets:
    """ This class holds all the methods to validate sets of brackets in a string """

    @staticmethod
    def find_valid_brackets(string):
        """
        This method checks the bracket sequence validity of string provided
        :param string: Input String
        :return: Bool True/False based on string processing
        """
        valid_brackets_dict = {'(': ')', '{': '}', '[': ']'}
        result_list = []

        conv_list = list(string)
        log.info(f"Test string -> List is : {conv_list}. List size is {len(conv_list)}")
        if len(conv_list) % 2 != 0:
            return False

        for j in range(int(len(conv_list)/2)):
            log.info(f"Running Iteration - {j+1}")
            for i in range(len(conv_list)):
                if i+1 < len(conv_list):
                    log.info(f"Testing element {conv_list[i]} at position {i} with element {conv_list[i+1]} at position {i+1}")
                    if conv_list[i] in valid_brackets_dict.keys() and conv_list[i+1] == valid_brackets_dict[conv_list[i]]:
                        log.info(f"Found {conv_list[i]} & {conv_list[i+1]} side-by-side...")
                        main_element = conv_list[i]
                        partner_element = conv_list[i+1]
                        result_list.append(str(main_element+partner_element))
                        conv_list.pop(i)
                        conv_list.pop(i)
                        log.info(f"Removed {main_element} & {partner_element} from the list... "
                                 f"List's current status is: {conv_list}")
                    else:
                        log.info(f"Element {conv_list[i]} & {conv_list[i+1]} are not pairs... Skipping")
                    if not conv_list:
                        log.info(f"Found all pairs! {result_list}")
                        return True

        if conv_list:
            log.info(f"Looks like there are items remaining in the list after cleanup : {conv_list}")
            return False

        return True


if __name__ == '__main__':
    vb = ValidBrackets()
    flag = vb.find_valid_brackets(string="(}{)")
    if not flag:
        log.info('String is unequal')
    else:
        log.info('String has balanced parentheses!')
