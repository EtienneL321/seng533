import { browser } from "k6/experimental/browser";
import { check } from "k6";
import exec from "k6/execution";

export const options = {
  scenarios: {
    scenario_10_VUs_5_Iterations: {
      executor: "per-vu-iterations",
      options: {
        browser: {
          type: "chromium",
        },
      },
      vus: 10,
      iterations: 5,
      maxDuration: "10m",
    },
  },
  thresholds: {
    checks: ["rate==1.0"],
  },
};

export default async function () {
  /* Create page element */
  const page = browser.newPage();

  try {
    /* Populate page element */
    await page.goto("https://djaq3qtxdz92e.cloudfront.net/");

    /* Get Buttons */
    const createUserButton = page.locator('//*[@id="create-user-button"]');
    const getUserButton = page.locator('//*[@id="get-user-button"]');
    const deleteUserButton = page.locator('//*[@id="delete-user-button"]');

    /**
     * Create user
     */
    let temp_id = exec.vu.idInInstance;
    let id = temp_id.toString();
    let username = "user" + id;
    page.locator('//*[@id="create-user-id-input"]').type(id);
    page.locator('//*[@id="create-user-name-input"]').type(username);

    await createUserButton.click();
    page.waitForSelector('//*[@id="create-user"]/h3');

    /**
     * Get user
     */
    page.locator('//*[@id="get-user-input"]').type(id);

    await getUserButton.click();
    page.waitForSelector('//*[@id="get-user-by-id"]/h3');

    /**
     * Check that user was successfully created
     */
    let ans = id + " . " + username;
    check(page, {
      userAddedSuccessfully: (p) =>
        p.locator('//*[@id="get-user-by-id"]/h3').textContent() == ans,
    });

    /**
     * Delete user
     */
    page.locator('//*[@id="delete-user-input"]').type(id);

    await deleteUserButton.click();
    page.waitForSelector('//*[@id="delete-user-by-id"]/div/h3');

    /**
     * Check that user was deleted successfulyy
     */
    let delAns = "User deleted";
    check(page, {
      userDeletedSuccessfully: (p) =>
        p.locator('//*[@id="delete-user-by-id"]/div/h3').textContent() ==
        delAns,
    });
  } finally {
    page.close();
  }
}

// export function handleSummary(data) {
//   return {
//     "summary.json": JSON.stringify(data), //the default data object
//   };
// }
