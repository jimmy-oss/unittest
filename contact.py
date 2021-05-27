class Contact():
    def __init__(self,first_name,last_name,number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    contact_list = [] # Empty contact list
 # Init method up here
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod

    def find_by_number(cls,number):
       
         

         for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact  
        