export default class TransactionObj {
    constructor(id, amount, vendor, categoryId,userId) {
      this.id = id;
      this.amount = amount;
      this.vendor = vendor;
      this.categoryId = categoryId;
      this.userId = userId
    }
  }