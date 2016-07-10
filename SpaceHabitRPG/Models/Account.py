from HabitBaseModel import HabitBaseModel
from AllDBFields import AccountFields
from datetime import datetime
from datetime import timezone
from Daily import Daily
from Hero import Hero
import DatabaseLayer
import uuid








#def get_account_by_userID(userID):
#  dbResults = DatabaseLayer.get_sorted_stuff_by_search(

class Account(HabitBaseModel):
  """
    This is a wrapper for the account data from the database
  """

  @classmethod
  def create_new_account_in_db(cls,loginPk=None):
    account = {
      AccountFields.LOGIN_PK_KEY: loginPk,
      AccountFields.REMINDER_TIME: -1,
      AccountFields.DAY_START:0,
      AccountFields.DEATH_GOLD_PENALTY: .25,
      AccountFields.HERO_LVL_PENALTY: 0,
      AccountFields.ZONE_LVL_PENALTY: "LVLRESTART",
      AccountFields.ENEMY_HEALED_ON_ATTACK: False,
      AccountFields.SELF_HEALED_ON_ATTACK: False,
      AccountFields.PERMA_DEATH: False,
      AccountFields.PUBLIC_ACCOUNT: False,
      AccountFields.PUBLIC_KEY: uuid.uuid4().hex,
      AccountFields.CREATE_DATE: datetime.utcnow().timestamp()
    }
    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    id = collection.insert_one(account).inserted_id
    return id

  @classmethod
  def get_dbFields(cls):
    return AccountFields

  @property
  def id(self):
    return self.dict[self.get_dbFields().PK_KEY]

      
  @property
  def lastCheckInTime(self):
    if AccountFields.LAST_CHECKIN_TIME in self.dict:
      return self.dict[self.get_dbFields().LAST_CHECKIN_TIME]
    return None


  @lastCheckInTime.setter
  def lastCheckInTime(self,value):
    self.dict[self.get_dbFields().LAST_CHECKIN_TIME] = value