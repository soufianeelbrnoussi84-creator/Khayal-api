const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  LevelFormat
} = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 320, after: 160 },
    children: [new TextRun({ text, bold: true, size: 32, color: "1a1a2e", font: "Arial" })]
  });
}

function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 120 },
    children: [new TextRun({ text, bold: true, size: 26, color: "16213e", font: "Arial" })]
  });
}

function body(text) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text, size: 22, font: "Arial" })]
  });
}

function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, size: 22, font: "Arial" })]
  });
}

function bugTable(file, bug, fix, lesson) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1800, 2520, 2520, 2520],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders, width: { size: 1800, type: WidthType.DXA },
            shading: { fill: "e8f4f8", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: file, bold: true, size: 20, font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "fde8e8", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: bug, size: 20, font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "e8fde8", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: fix, size: 20, font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "fff8e8", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: lesson, size: 20, font: "Arial" })] })]
          }),
        ]
      })
    ]
  });
}

function tableHeader() {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1800, 2520, 2520, 2520],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders, width: { size: 1800, type: WidthType.DXA },
            shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "File", bold: true, size: 22, color: "FFFFFF", font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "Bug / Issue", bold: true, size: 22, color: "FFFFFF", font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "Fix", bold: true, size: 22, color: "FFFFFF", font: "Arial" })] })]
          }),
          new TableCell({
            borders, width: { size: 2520, type: WidthType.DXA },
            shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "Lesson Learned", bold: true, size: 22, color: "FFFFFF", font: "Arial" })] })]
          }),
        ]
      })
    ]
  });
}

function spacer() {
  return new Paragraph({ spacing: { before: 120, after: 120 }, children: [new TextRun("")] });
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      }
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: "1a1a2e" },
        paragraph: { spacing: { before: 320, after: 160 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "16213e" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // Title
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 320 },
        children: [new TextRun({ text: "Khayal \u062e\u064a\u0627\u0644 \u2014 Bugs & Lessons Learned", bold: true, size: 48, color: "1a1a2e", font: "Arial" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 480 },
        children: [new TextRun({ text: "A complete record of every bug, issue, and lesson from building the Khayal API", size: 22, color: "666666", font: "Arial" })]
      }),

      // Section 1
      heading1("1. models/user.py"),
      tableHeader(),
      bugTable("user.py", "date_of_birth: str — wrong type", "Changed to date from datetime module", "Always use proper Python types. str for dates loses validation and PostgreSQL type benefits."),
      spacer(),
      bugTable("user.py", "is_active: str — wrong type", "Changed to bool with default=True", "Boolean fields must use bool not str. Always set a default for automatic fields."),
      spacer(),
      bugTable("user.py", "created_at: str — wrong type", "Changed to datetime with default_factory=datetime.utcnow", "Use datetime for timestamps. default_factory runs fresh on each object creation unlike default=datetime.utcnow() which runs once at startup."),
      spacer(),
      bugTable("user.py", "import datetime then datetime.datetime.utcnow", "from datetime import date, datetime — then use datetime.utcnow directly", "When importing with 'from x import y', use y directly without repeating the module name."),
      spacer(),

      // Section 2
      heading1("2. schemas/user.py"),
      tableHeader(),
      bugTable("schemas/user.py", "UserResponse missing model_config", "Added model_config = {'from_attributes': True}", "Output schemas reading from database objects need from_attributes=True. Input schemas don't need it."),
      spacer(),
      bugTable("schemas/user.py", "model_config placed in middle of class", "Moved to top of class before all fields", "Class configuration should always be at the top before field definitions."),
      spacer(),
      bugTable("schemas/user.py", "created_at: date instead of datetime", "Changed to datetime", "date only stores day/month/year. datetime stores full timestamp including time."),
      spacer(),
      bugTable("schemas/user.py", "Unused imports: Optional, Field", "Removed unused imports", "Clean code means no unused imports. Only import what you actually use."),
      spacer(),

      // Section 3
      heading1("3. security/user.py"),
      tableHeader(),
      bugTable("security/user.py", "verify_password parameter named hashed_password — conflicts with function name above", "Renamed parameter to hash_password", "Never name a variable the same as an existing function. Python will get confused."),
      spacer(),
      bugTable("security/user.py", "to_encod typo in create_access_token", "Renamed to to_encode", "Typos in variable names cause NameError bugs. Always double check variable names."),
      spacer(),
      bugTable("security/user.py", "bcrypt version incompatibility with passlib", "pip install bcrypt==4.0.1", "Library version conflicts are common. Always check compatibility between related packages."),
      spacer(),

      // Section 4
      heading1("4. services/user.py"),
      tableHeader(),
      bugTable("services/user.py", "Depends(get_session) used in service — belongs in routes only", "Removed Depends, session passed as plain parameter from route", "Depends is a FastAPI tool for routes only. Services receive the session as a plain parameter."),
      spacer(),
      bugTable("services/user.py", "Email check: if email in User.email — wrong logic", "Changed to: if check_email: raise HTTPException", "User.email is a column definition not a value. Always use the query result variable to check existence."),
      spacer(),
      bugTable("services/user.py", "login: querying database to check password", "Used verify_password(plain, hashed) instead", "Hashed passwords cannot be compared directly in SQL queries. Always use verify_password function."),
      spacer(),

      // Section 5
      heading1("5. routes/user.py"),
      tableHeader(),
      bugTable("routes/user.py", "Used FastAPI and app = FastAPI() in routes file", "Replaced with APIRouter and router = APIRouter()", "Routes files use APIRouter not the full FastAPI app. Only main.py creates the app."),
      spacer(),
      bugTable("routes/user.py", "Function name login conflicts with imported login from services", "Renamed route function to user_login", "Never name a route function the same as an imported service function. Python will call itself recursively."),
      spacer(),
      bugTable("routes/user.py", "response_model=UserLogin on login endpoint", "Changed to response_model=TokenResponse", "Login returns a token not a user object. Always match response_model to what the function actually returns."),
      spacer(),

      // Section 6
      heading1("6. models/product.py"),
      tableHeader(),
      bugTable("product.py", "Product class defined before ProductSize and ProductCategory enums", "Moved enums to top before the Product class", "Python reads top to bottom. Always define enums before the model that uses them."),
      spacer(),
      bugTable("product.py", "size: str instead of ProductSize enum", "Changed to size: ProductSize", "Always use your custom enum types for enum fields, not plain str."),
      spacer(),
      bugTable("product.py", "is_available: bool = Field(default=None)", "Changed to Field(default=True)", "None for a bool field causes NotNullViolation in PostgreSQL. Always use True or False as default."),
      spacer(),
      bugTable("product.py", "Comma after enum values e.g. pending='pending',", "Removed trailing commas from enum values", "Trailing comma in enum creates a tuple ('pending',) not a string 'pending'. Never add commas to enum values."),
      spacer(),

      // Section 7
      heading1("7. services/product.py"),
      tableHeader(),
      bugTable("services/product.py", "product_data.items() called on schema object", "Saved model_dump result first: data = product_data.model_dump(exclude_unset=True) then data.items()", "You cannot call .items() directly on a Pydantic schema. First convert to dict with model_dump()."),
      spacer(),
      bugTable("services/product.py", "session.refresh(delete) after deleting object", "Removed session.refresh — object no longer exists after delete", "You cannot refresh a deleted object. After session.delete() and commit(), just return the success message."),
      spacer(),

      // Section 8
      heading1("8. services/order.py"),
      tableHeader(),
      bugTable("services/order.py", "Stock check: if order.quantity >= product.quantity — wrong direction", "Changed to if order.quantity > product.quantity", "Raise error when order quantity EXCEEDS stock, not when it is less or equal. Logic was inverted."),
      spacer(),
      bugTable("services/order.py", "total_price not passed to Order object", "Added total_price=total inside Order(...)", "Always include all required fields when creating a model object. Missing fields cause NotNullViolation."),
      spacer(),
      bugTable("services/order.py", "OrderStatus imported from schemas instead of models", "from models.order import Order, OrderStatus", "Enums are defined in models not schemas. Always import from the correct source."),
      spacer(),
      bugTable("services/order.py", "Finding order by Order.product_id instead of Order.id", "Changed to Order.id == order_id", "order_id refers to the order's own ID, not the product ID. Always query by the correct field."),
      spacer(),

      // Section 9
      heading1("9. routes/product.py & routes/order.py"),
      tableHeader(),
      bugTable("routes/product.py", "Function named get_product conflicts with imported get_product from services", "Renamed route functions to all_product, all_orders etc.", "Route function names must not match imported service function names."),
      spacer(),
      bugTable("routes/product.py", "response_model=ProductResponse for get_product_by_name which returns a list", "Changed to response_model=list[ProductResponse]", "When a function returns multiple items use list[Schema] not just Schema."),
      spacer(),
      bugTable("routes/order.py", "create_order had admin auth — should be public", "Removed Depends(get_current_admin) from create_order", "Customers don't need to login to place an order. Only admin-only actions need authentication."),
      spacer(),
      bugTable("routes/order.py", "update_order_status called with wrong parameter order", "Matched service signature: update_order_status(session, order_data, order_id)", "Always check the service function signature before calling it from the route."),
      spacer(),

      // Section 10 - Key Concepts
      heading1("10. Key Concepts Learned"),
      heading2("Models vs Schemas"),
      bullet("Model = database table. Schema = input/output shape."),
      bullet("Never query a schema from the database — always query the Model."),
      bullet("Output schemas need from_attributes=True. Input schemas don't."),
      spacer(),
      heading2("Routes vs Services"),
      bullet("Routes = the waiter. Takes the order, passes to chef, returns result."),
      bullet("Services = the chef. Does all the actual business logic."),
      bullet("Routes should have minimum logic — just call the service and return."),
      spacer(),
      heading2("Database"),
      bullet("engine = permanent bridge to PostgreSQL, created once at startup."),
      bullet("session = temporary workspace per request, opened and closed each time."),
      bullet("Depends(get_session) belongs in routes, not services."),
      spacer(),
      heading2("Python Types"),
      bullet("date = day/month/year only. datetime = full timestamp with time."),
      bullet("default=datetime.utcnow() runs once. default_factory=datetime.utcnow runs fresh each time."),
      bullet("bool fields must be True/False never None — PostgreSQL will reject null."),
      bullet("Phone numbers must be str not int — int removes leading zeros."),
      spacer(),
      heading2("JWT & Security"),
      bullet("Never store password in JWT token — token can be decoded by anyone."),
      bullet("JWT contains: email (sub), role, expiry time (exp)."),
      bullet("Always hash passwords with bcrypt before saving to database."),
      bullet("verify_password compares plain to hashed — never query by password."),
      spacer(),

      // Final note
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 480, after: 0 },
        children: [new TextRun({ text: "Khayal \u062e\u064a\u0627\u0644 \u2014 Wear your dream \uD83C\uDDF2\uD83C\uDDE6", bold: true, size: 28, color: "1a1a2e", font: "Arial" })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/khayal_bugs_and_lessons.docx', buffer);
  console.log('Done!');
});